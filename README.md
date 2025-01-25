# Projeto ETL para Extração de Dados da CoinGecko

Este projeto é um pipeline **ETL** (Extract, Transform, Load) para coletar, processar e armazenar dados da plataforma **CoinGecko**. Ele foi desenvolvido em **Python** para facilitar a integração e a automação do fluxo de dados. Este projeto foi criado para fins de **portfólio** e está disponível no meu site pessoal ([alanavelar.com](https://alanavelar.com)).

## Funcionalidades

- **Extração**: Coleta de dados da API da CoinGecko.
- **Transformação**: Processamento, limpeza e armazenamento dos dados.
- **Carregamento**: Carregamento dos dados em plataforma de visualização.

## Requisitos

- **Python 3.8 ou superior**
- Conta de desenvolvedor na **CoinGecko** (para acessar a API)
- **Docker** (opcional, caso prefira rodar em contêiner)

### Bibliotecas Necessárias

As dependências podem ser instaladas usando o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

As principais bibliotecas utilizadas incluem:

- `requests` - Para interagir com a API da CoinGecko.
- `pandas` - Para manipulação e transformação de dados.
- `sqlalchemy` - Para conexão com bancos de dados.

## Configuração

1. **Clone este repositório:**

```bash
git clone https://github.com/tameimpalan/PythonETLCoinGecko.git
cd PythonETLCoinGecko
```

2. **Configure as variáveis de ambiente** no arquivo `.env`. Um exemplo está disponível em `.env.example`:

```env
DATABASE_URL=postgresql://usuario:senha@localhost:5432/seubanco
```

3. **(Opcional)** Construa e rode o projeto com Docker:

```bash
docker build -t PythonETLCoinGecko .
docker run --env-file .env PythonETLCoinGecko
```

## Estrutura do Projeto

```plaintext
/
├── src/
│   ├── extract.py  # Extração de dados da API CoinGecko
│   ├── transform.py  # Limpeza e processamento dos dados
│   └── load.py  # Carregamento para o banco de dados
├── .env.example  # Exemplo de configuração de variáveis de ambiente
├── requirements.txt  # Dependências do projeto
└── README.md  # Documentação do projeto
```

## Execução

1. **Certifique-se de que todas as dependências estão instaladas.**

2. **Execute o pipeline:**

```bash
python src/extract.py
python src/transform.py
python src/load.py
```

3. **Verifique os dados processados** no destino configurado (banco de dados ou arquivo).

## Limite de Requisições da API

A API da **CoinGecko** possui o seguinte limite de requisições no plano gratuito:
- **100 requisições por minuto.**
- **Sem limite diário definido**, desde que respeitado o limite de 100 chamadas por minuto.

Se você exceder este limite, suas requisições podem ser **temporariamente bloqueadas**. Para lidar com isso, recomenda-se implementar pausas (`time.sleep`) entre as chamadas ou adotar um plano comercial oferecido pela CoinGecko.

## Melhorias Futuras

- **Implementar logs estruturados** para monitoramento.
- **Escalar o pipeline** com orquestrador mais robusto (como Airflow).

### Contato

Este projeto foi desenvolvido para fins de **portfólio**. Entre em contato pelo email: [contato@alanavelar.com](mailto:contato@alanavelar.com).