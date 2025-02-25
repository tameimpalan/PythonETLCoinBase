import os
import pandas as pd
import logging
from dotenv import load_dotenv
from google.cloud import storage

# Configuração do logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Carregar variáveis de ambiente
load_dotenv()
os.environ["SILVER_BUCKET_NAME"] = os.getenv("SILVER_BUCKET_NAME")
os.environ["BRONZE_BUCKET_NAME"] = os.getenv("BRONZE_BUCKET_NAME")

credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
base_dir = os.path.dirname(os.path.dirname(__file__))
absolute_credentials_path = os.path.join(base_dir, credentials_path)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = absolute_credentials_path

logging.info(f"Loaded environment variables. Bronze: {os.environ['BRONZE_BUCKET_NAME']}, Silver: {os.environ['SILVER_BUCKET_NAME']}")

def transform_obtained_data(df):
    """Aplica a transformação das colunas e renomeia os campos."""
    logging.info("Transforming data...")

    translated_columns = {
        "id": "id",
        "symbol": "simbolo",
        "name": "nome",
        "image": "imagem",
        "current_price": "preco_atual",
        "market_cap": "valor_mercado",
        "market_cap_rank": "ranking_mercado",
        "fully_diluted_valuation": "valorizacao_diluida_total",
        "total_volume": "volume_total",
        "high_24h": "maior_preco_24h",
        "low_24h": "menor_preco_24h",
        "price_change_24h": "variacao_preco_24h",
        "price_change_percentage_24h": "variacao_percentual_24h",
        "market_cap_change_24h": "mudanca_valor_mercado_24h",
        "market_cap_change_percentage_24h": "mudanca_percentual_mercado_24h",
        "circulating_supply": "quantidade_circulacao",
        "total_supply": "quantidade_total",
        "max_supply": "quantidade_maxima",
        "ath": "preco_mais_alto",
        "ath_change_percentage": "queda_percentual_ath",
        "ath_date": "data_ath",
        "atl": "preco_mais_baixo",
        "atl_change_percentage": "aumento_percentual_atl",
        "atl_date": "data_atl",
        "roi": "retorno_investimento",
        "last_updated": "ultima_atualizacao",
        "created_at": "criado_em"
    }

    df = df.rename(columns=translated_columns)
    
    return df

def update_silver(bronze_bucket, silver_bucket, bronze_prefix, silver_file):
    """Realiza a leitura dos arquivos na camada Bronze e os adiciona à Silver, removendo duplicatas."""
    logging.info("Starting Silver update...")

    client = storage.Client()
    bucket = client.bucket(bronze_bucket)

    logging.info("Listing blobs in Bronze bucket...")
    blobs = list(bucket.list_blobs(prefix=bronze_prefix))
    logging.info(f"Found {len(blobs)} files in Bronze.")

    try:
        silver_path = f"gs://{silver_bucket}/{silver_file}"
        logging.info(f"Checking if Silver file exists: {silver_path}")

        silver_df = pd.read_parquet(silver_path, storage_options={"anon": False})
        arquivos_processados = set(silver_df["arquivo_origem"].unique())
        logging.info(f"Loaded Silver file, {len(silver_df)} records found.")

    except Exception as e:
        logging.warning(f"Silver file not found or could not be read: {e}")
        silver_df = pd.DataFrame()
        arquivos_processados = set()

    novos_dfs = []
    for blob in blobs:
        if blob.name.endswith(".parquet") and blob.name not in arquivos_processados:
            logging.info(f"Processing new file: {blob.name}")
            df = pd.read_parquet(f"gs://{bronze_bucket}/{blob.name}", storage_options={"anon": False})
            df["arquivo_origem"] = blob.name  # Adiciona o nome do arquivo como referência
            novos_dfs.append(df)

    if novos_dfs:
        logging.info("Concatenating new data...")
        bronze_df = pd.concat(novos_dfs, ignore_index=True)
        logging.info(f"New data count: {len(bronze_df)} records.")

        transformed_df = transform_obtained_data(bronze_df)
        logging.info("Transformation completed.")

        updated_df = pd.concat([silver_df, transformed_df], ignore_index=True).drop_duplicates()
        logging.info(f"Updated Silver count: {len(updated_df)} records.")

        updated_df.to_parquet(silver_path, engine="pyarrow", index=False, storage_options={"anon": False})
        logging.info(f"Silver table updated: {silver_path}")
    else:
        logging.info("No new files to process.")

if __name__ == "__main__":
    logging.info("Starting Silver processing job...")

    bronze_bucket_name = os.getenv("BRONZE_BUCKET_NAME")
    silver_bucket_name = os.getenv("SILVER_BUCKET_NAME")

    bronze_prefix = "coingecko/"
    silver_file = "coingecko/mercados.parquet"

    if bronze_bucket_name and silver_bucket_name:
        update_silver(bronze_bucket_name, silver_bucket_name, bronze_prefix, silver_file)
    else:
        logging.error("BRONZE_BUCKET_NAME or SILVER_BUCKET_NAME not properly set in .env")
