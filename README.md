# Projeto de Extração de Dados da Coinbase API com Python

Este é um projeto inicial que utiliza a API da Coinbase para realizar a extração de dados financeiros relacionados a criptomoedas. Ele foi desenvolvido em Python, utilizando a biblioteca `requests` para realizar chamadas à API.

## Funcionalidades

- Autenticação e conexão com a API da Coinbase.
- Extração de dados de preços, transações e outros recursos disponíveis na API.
- Armazenamento e organização dos dados em um formato estruturado para futuras análises.

## Tecnologias Utilizadas

- **Linguagem**: Python 3.9+
- **Bibliotecas**:
  - `requests` para realizar chamadas à API.
  - `json` para manipulação de dados retornados.

## Requisitos

Certifique-se de ter os seguintes itens instalados:

1. Python 3.9 ou superior.
2. Gerenciador de pacotes `pip` (geralmente incluso na instalação do Python).
3. Uma conta na [Coinbase](https://www.coinbase.com/) com acesso às chaves de API.

## Instalação

1. Clone este repositório para a sua máquina local:

   ```bash
   git clone https://github.com/seuusuario/coinbase-api-extraction.git
   cd coinbase-api-extraction
   ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências necessárias:

   ```bash
   pip install requests
   ```

## Configuração

1. Crie um arquivo `.env` na raiz do projeto e adicione suas credenciais da API da Coinbase:

   ```env
   COINBASE_API_KEY=your_api_key
   COINBASE_API_SECRET=your_api_secret
   ```

2. Certifique-se de manter este arquivo seguro e não compartilhá-lo publicamente.

## Uso

Um exemplo de uso básico pode ser encontrado no arquivo `main.py`. Para executar o script:

```bash
python main.py
```

### Exemplo de Chamada à API

```python
import requests
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()

API_KEY = os.getenv("COINBASE_API_KEY")
API_SECRET = os.getenv("COINBASE_API_SECRET")
BASE_URL = "https://api.coinbase.com/v2"

# Exemplo: Buscar preço atual do Bitcoin
response = requests.get(f"{BASE_URL}/prices/BTC-USD/spot", headers={
    "Authorization": f"Bearer {API_KEY}"
})

data = response.json()
print(data)
```

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões ou encontrar bugs, abra uma issue ou envie um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

# PythonETLCoinBase
