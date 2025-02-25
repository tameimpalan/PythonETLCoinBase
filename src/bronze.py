import requests
import os
import pandas as pd
import io
import logging
from dotenv import load_dotenv
from google.cloud import storage
from datetime import datetime, timezone, timedelta

# Configuração do logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Carregar variáveis de ambiente
load_dotenv()
os.environ["COINGECKO_API_KEY"] = os.getenv("COINGECKO_API_KEY")
os.environ["BRONZE_BUCKET_NAME"] = os.getenv("BRONZE_BUCKET_NAME")

credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
base_dir = os.path.dirname(os.path.dirname(__file__))
absolute_credentials_path = os.path.join(base_dir, credentials_path)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = absolute_credentials_path

def extract_data_from_coingecko(timestamp):
    """ Extrai os dados da API do CoinGecko e adiciona um timestamp. """
    logging.info("Extracting data from CoinGecko API...")
    url = "https://api.coingecko.com/api/v3/coins/markets"

    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 250,
        "page": 1,
        "x_cg_demo_api_key": os.environ.get("COINGECKO_API_KEY")
    }
    
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        for item in data:
            item["created_at"] = timestamp
        logging.info(f"Successfully extracted {len(data)} records.")
        return data
    else:
        logging.error(f"Error on fetching API data: {response.status_code}")
        logging.error(f"Error object: {response.json()}")
        return []

def upload_parquet_to_bronze(bucket_name, data, destination_blob_name):
    """ Converte os dados para Parquet e envia para o Cloud Storage na camada Bronze. """
    try:
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        df = pd.DataFrame(data)

        # Converte todas as colunas para string antes de salvar
        df = df.astype(str)

        parquet_buffer = io.BytesIO()
        df.to_parquet(parquet_buffer, engine="pyarrow", index=False)
        parquet_buffer.seek(0)

        blob.upload_from_file(parquet_buffer, content_type="application/octet-stream")
        
        logging.info(f"File successfully uploaded to Bronze: {bucket_name}/{destination_blob_name}")
    except Exception as e:
        logging.error(f"Error when uploading to Cloud Storage: {e}")

if __name__ == "__main__":
    logging.info("Starting Bronze processing job...")

    timestamp = (datetime.now(timezone.utc) - timedelta(hours=3))
    year, month, day = timestamp.strftime("%Y"), timestamp.strftime("%m"), timestamp.strftime("%d")
    formatted_timestamp = timestamp.strftime("%Y%m%d%H%M%S")

    bronze_bucket_name = os.getenv("BRONZE_BUCKET_NAME")    
    bronze_blob_name = f"coingecko/{year}/{month}/{day}/markets_{formatted_timestamp}.parquet"

    data = extract_data_from_coingecko(timestamp)
    if data and bronze_bucket_name:
        upload_parquet_to_bronze(bronze_bucket_name, data, bronze_blob_name)
    else:
        logging.warning("No data extracted or BRONZE_BUCKET_NAME not properly set in .env")
