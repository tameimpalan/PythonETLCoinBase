# Projeto ETL para Extração de Dados da CoinGecko

Este projeto é um pipeline **ETL** (Extract, Transform, Load) para coletar, processar e armazenar dados da plataforma **CoinGecko**. Ele foi desenvolvido em **Python** para facilitar a integração e a automação do fluxo de dados. Este projeto foi criado para fins de **portfólio** e está disponível no meu site pessoal ([alanavelar.com](https://alanavelar.com)).

## Funcionalidades

- **Extração**: Coleta de dados da API da CoinGecko.
- **Transformação**: Processamento, limpeza e armazenamento dos dados.
- **Carregamento**: Carregamento dos dados em plataforma de visualização.

## Requisitos

- **Python 3.8 ou superior**
- **Virtual Environment (venv)** para isolar as dependências do projeto.
- Conta de desenvolvedor na **CoinGecko** (opcional, para autenticação).
- **Docker** (opcional, caso prefira rodar em contêiner).

### Benefícios da Autenticação na API da CoinGecko

A autenticação na API da CoinGecko é opcional, mas oferece o benefício de aumentar o limite de requisições de 100 para 200 chamadas por minuto. Para utilizar a autenticação, você deve gerar uma chave de API no site da CoinGecko e configurá-la como uma variável de ambiente. Consulte o guia oficial para mais detalhes sobre como gerar sua chave de API: [CoinGecko - User Guide](https://support.coingecko.com/hc/en-us/articles/21880397454233-User-Guide-How-to-sign-up-for-CoinGecko-Demo-API-and-generate-an-API-key).

Exemplo de configuração no arquivo `.env`:

```env
COINGECKO_API_KEY=SUA_API_KEY
```

Ao utilizar a chave de API, ela deve ser incluída nos parâmetros da requisição, como no exemplo abaixo:

```python
coingecko_api_key = os.getenv("COINGECKO_API_KEY")

params = {
    "x_cg_pro_api_key": coingecko_api_key,
    # Outros parâmetros aqui...
}
```

## Configuração

1. **Clone este repositório:**

```bash
git clone https://github.com/tameimpalan/PythonETLCoinGecko.git
cd PythonETLCoinGecko
```

2. **Crie e ative um ambiente virtual (venv):**

```bash
python -m venv venv
# Ativar no Windows
venv\Scripts\activate
# Ativar no Linux/Mac
source venv/bin/activate
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Configure as variáveis de ambiente no arquivo ****\`\`****.** Um exemplo está disponível em `.env.example`:

```env
COINGECKO_API_KEY=CG-E6sJJSfPrJAfx9ZJHeWpo3D4
DATABASE_URL=postgresql://usuario:senha@localhost:5432/seubanco
```

5. **(Opcional) Construa e rode o projeto com Docker:**

```bash
docker build -t PythonETLCoinGecko .
docker run --env-file .env PythonETLCoinGecko
```

## Estrutura do Projeto

```plaintext
/
├── pipeline.py  # Pipeline completo de extração, transformação e carregamento
├── .env.example  # Exemplo de configuração de variáveis de ambiente
├── requirements.txt  # Dependências do projeto
└── README.md  # Documentação do projeto
```

## Execução

1. **Certifique-se de que todas as dependências estão instaladas.**

2. **Execute o pipeline:**

```bash
python pipeline.py
```

3. **Verifique os dados processados** no destino configurado (banco de dados ou arquivo).

## Limite de Requisições da API

A API da **CoinGecko** possui os seguintes limites de requisições:

- **Plano público (sem autenticação):** 100 requisições por minuto.
- **Plano com autenticação:** 200 requisições por minuto (necessário passar a chave `x_cg_pro_api_key` nos parâmetros da requisição).

Se você exceder este limite, suas requisições podem ser **temporariamente bloqueadas**. Para lidar com isso, recomenda-se implementar pausas (`time.sleep`) entre as chamadas ou configurar a chave de autenticação para aproveitar o limite maior.

## Melhorias Futuras

- **Implementar logs estruturados** para monitoramento.
- **Escalar o pipeline** com orquestrador mais robusto (como Airflow).

### Contato

Este projeto foi desenvolvido para fins de **portfólio**. Entre em contato pelo email: [contato@alanavelar.com](mailto\:contato@alanavelar.com).

