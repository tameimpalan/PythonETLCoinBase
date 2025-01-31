# Extração de dados da API Coingecko e salvamento no GCP
import requests
import os
import json
from pprint import pprint
from dotenv import load_dotenv
from google.cloud import storage
from datetime import datetime, timezone, timedelta

# Carregar variáveis de ambiente
load_dotenv()
os.environ["COINGECKO_API_KEY"] = os.getenv("COINGECKO_API_KEY")
os.environ["GCP_BUCKET_NAME"] = os.getenv("GCP_BUCKET_NAME")

credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

base_dir = os.path.dirname(os.path.dirname(__file__))
absolute_credentials_path = os.path.join(base_dir, credentials_path)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = absolute_credentials_path

print(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))

def extract_data_from_coingecko():
    url = "https://api.coingecko.com/api/v3/coins/markets"

    params = {
        "vs_currency": "usd",           # Moeda de referência
        "order": "market_cap_desc",     # Ordenar por capitalização de mercado
        "per_page": 100,                  # Quantidade de criptomoedas
        "page": 1,                      # Página inicial
        "x_cg_demo_api_key": os.environ.get("COINGECKO_API_KEY")
    }
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Erro na API: {response.status_code}")
        print(f"Erro: {response.json()}")
        return {}

def transform_obtained_data(data, timestamp):
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
        "last_updated": "ultima_atualizacao"
    }

    return [
        {**{translated_columns.get(k, k): v for k, v in item.items()}, "created_at": timestamp}
        for item in data
    ]

def upload_to_gcp(bucket_name, data, destination_blob_name):
    """Faz upload dos dados transformados diretamente para o GCP sem salvar localmente."""
    try:
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_string(json.dumps(data, indent=4, ensure_ascii=False), content_type="application/json")
        print(f"Arquivo enviado para '{bucket_name}/{destination_blob_name}' com sucesso!")
    except Exception as e:
        print(f"Erro ao fazer upload para o GCP: {e}")


if __name__ == "__main__":
    data = extract_data_from_coingecko()
    
    timestamp = datetime.now(timezone.utc) - timedelta(hours=3)
    iso_timestamp = timestamp.isoformat()
    str_timestamp = timestamp.strftime("%Y%m%d%H%M%S")

    transformed_data = transform_obtained_data(data, iso_timestamp)

    gcp_bucket_name = os.getenv("GCP_BUCKET_NAME")
    
    gcp_destination_blob = f"transformed_data/coingecko_markets_data_{str_timestamp}.json"

    if gcp_bucket_name:
        upload_to_gcp(gcp_bucket_name, transformed_data, gcp_destination_blob)
    else:
        print("GCP_BUCKET_NAME não configurado no .env")
