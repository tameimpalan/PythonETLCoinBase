# Extração de dados da API Coinbase
import requests

def extract_dados_coingecko():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",          # Moeda de referência
        "order": "market_cap_desc",    # Ordenar por capitalização de mercado
        "per_page": 100,               # Quantidade de criptomoedas
        "page": 1,                     # Página inicial
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        # Retorna um dicionário com o nome e preço das criptomoedas
        return {coin['symbol'].upper(): coin['current_price'] for coin in data}
    else:
        print(f"Erro na API: {response.status_code}")
        return {}

# Obter as top 100 criptomoedas e seus preços
top_100_prices = get_top_100_cryptos()
print(top_100_prices)

