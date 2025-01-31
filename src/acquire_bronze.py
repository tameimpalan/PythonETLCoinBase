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
        print(f"Error on fetching API data: {response.status_code}")
        print(f"Error object: {response.json()}")
        return {}

def upload_to_gcp(bucket_name, data, destination_blob_name):
    try:
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_string(json.dumps(data, indent=4, ensure_ascii=False), content_type="application/json")
        print(f"File sent to bronze layer on bucket '{bucket_name}/{destination_blob_name}'.")
    except Exception as e:
        print(f"Error when uploading to Cloud Storage: {e}")

if __name__ == "__main__":
    data = extract_data_from_coingecko()
    
    timestamp = (datetime.now(timezone.utc) - timedelta(hours=3)).strftime("%Y%m%d%H%M%S")
    print(timestamp)

    gcp_bucket_name = os.getenv("GCP_BUCKET_NAME")    
    gcp_destination_blob = f"coingecko/markets_{timestamp}.json"

    if gcp_bucket_name:
        upload_to_gcp(gcp_bucket_name, data, gcp_destination_blob)
    else:
        print("GCP_BUCKET_NAME not properly set on .env")
