# Extração de dados da API Coinbase
import requests
import os
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

def extract_data_from_coingecko():
    url = "https://api.coingecko.com/api/v3/coins/markets"

    coingecko_api_key = os.getenv("COINGECKO_API_KEY")
    params = {
        "vs_currency": "usd",          # Moeda de referência
        "order": "market_cap_desc",    # Ordenar por capitalização de mercado
        "per_page": 1,               # Quantidade de criptomoedas
        "page": 1,                     # Página inicial
        "x_cg_demo_api_key": coingecko_api_key
    }
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers,params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Erro na API: {response.status_code}")
        return {}
    
def transform_obtained_data(data):
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
        {translated_columns.get(k, k): v for k, v in item.items()} for item in data
    ]


if __name__ == "__main__":
    top100 = extract_data_from_coingecko()
    transformed_top100 = transform_obtained_data(top100)
    pprint(transformed_top100)

