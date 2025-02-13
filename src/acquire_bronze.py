import requests
import os
import pandas as pd
import io
from dotenv import load_dotenv
from google.cloud import storage
from datetime import datetime, timezone, timedelta

# Carregar variáveis de ambiente
load_dotenv()
os.environ["COINGECKO_API_KEY"] = os.getenv("COINGECKO_API_KEY")
os.environ["BRONZE_BUCKET_NAME"] = os.getenv("BRONZE_BUCKET_NAME")

credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
base_dir = os.path.dirname(os.path.dirname(__file__))
absolute_credentials_path = os.path.join(base_dir, credentials_path)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = absolute_credentials_path

def extract_data_from_coingecko():
    url = "https://api.coingecko.com/api/v3/coins/markets"

    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 100,
        "page": 1,
        "x_cg_demo_api_key": os.environ.get("COINGECKO_API_KEY")
    }
    
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error on fetching API data: {response.status_code}")
        print(f"Error object: {response.json()}")
        return []

def upload_parquet_to_bronze(bucket_name, data, destination_blob_name):
    try:
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        df = pd.DataFrame(data)

        parquet_buffer = io.BytesIO()
        df.to_parquet(parquet_buffer, engine="pyarrow", index=False)
        parquet_buffer.seek(0)

        blob.upload_from_file(parquet_buffer, content_type="application/octet-stream")
        
        print(f"File sent to bronze layer on bucket '{bucket_name}/{destination_blob_name}'.")
    except Exception as e:
        print(f"Error when uploading to Cloud Storage: {e}")

if __name__ == "__main__":
    data = extract_data_from_coingecko()
    timestamp = (datetime.now(timezone.utc) - timedelta(hours=3))
    year, month, day = timestamp.strftime("%Y"), timestamp.strftime("%m"), timestamp.strftime("%d")
    formatted_timestamp = timestamp.strftime("%Y%m%d%H%M%S")

    bronze_bucket_name = os.getenv("BRONZE_BUCKET_NAME")    
    bronze_blob_name = f"coingecko/{year}/{month}/{day}/markets_{formatted_timestamp}.parquet"

    if data and bronze_bucket_name:
        upload_parquet_to_bronze(bronze_bucket_name, data, bronze_blob_name)
    else:
        print("No data extracted or BRONZE_BUCKET_NAME not properly set on .env")
