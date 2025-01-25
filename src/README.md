# Dicionário de Dados do Output do Endpoint da CoinGecko

Este documento descreve os campos retornados pelo endpoint da CoinGecko utilizado para listar as 100 principais criptomoedas por valor de mercado: `https://api.coingecko.com/api/v3/coins/markets`. O objetivo é fornecer uma visão clara e organizada dos dados disponíveis, detalhando cada campo com sua descrição, tipo de dado e um `Campo (PT-BR)` sugerido para uso em bancos de dados. Isso garante consistência e padronização no tratamento dessas informações em seu projeto.

| Campo                        | `Campo (PT-BR)`                | Descrição                                                                                         | Tipo       |
|------------------------------|---------------------------------|-------------------------------------------------------------------------------------------------|------------|
| `id`                         | `id`                           | Identificador único da criptomoeda.                                                             | String     |
| `symbol`                     | `simbolo`                      | Símbolo ou ticker da criptomoeda (ex.: "BTC").                                                  | String     |
| `name`                       | `nome`                         | Nome completo da criptomoeda (ex.: "Bitcoin").                                                  | String     |
| `image`                      | `imagem`                       | URL da imagem associada à criptomoeda.                                                          | String     |
| `current_price`              | `preco_atual`                  | Preço atual da criptomoeda na moeda base (ex.: USD, BRL).                                        | Float      |
| `market_cap`                 | `valor_mercado`                | Valor total de mercado da criptomoeda.                                                          | Float      |
| `market_cap_rank`            | `ranking_mercado`              | Posição da criptomoeda no ranking de mercado.                                                   | Inteiro    |
| `fully_diluted_valuation`    | `valorizacao_diluida_total`    | Valorização máxima com base no fornecimento máximo de moedas.                                    | Float      |
| `total_volume`               | `volume_total`                 | Volume total negociado nas últimas 24 horas.                                                   | Float      |
| `high_24h`                   | `maior_preco_24h`              | Maior preço da criptomoeda nas últimas 24 horas.                                              | Float      |
| `low_24h`                    | `menor_preco_24h`              | Menor preço da criptomoeda nas últimas 24 horas.                                              | Float      |
| `price_change_24h`           | `variacao_preco_24h`           | Variação absoluta no preço nas últimas 24 horas.                                        | Float      |
| `price_change_percentage_24h`| `variacao_percentual_24h`      | Percentual de variação do preço nas últimas 24 horas.                                      | Float      |
| `market_cap_change_24h`      | `mudanca_valor_mercado_24h`    | Mudança no valor de mercado absoluto nas últimas 24 horas.                                     | Float      |
| `market_cap_change_percentage_24h`| `mudanca_percentual_mercado_24h`| Percentual de mudança no valor de mercado nas últimas 24 horas.                              | Float      |
| `circulating_supply`         | `quantidade_circulacao`        | Quantidade de moedas em circulação.                                                            | Float      |
| `total_supply`               | `quantidade_total`             | Quantidade total de moedas emitidas.                                                             | Float      |
| `max_supply`                 | `quantidade_maxima`            | Quantidade máxima de moedas planejadas.                                                         | Float      |
| `ath`                        | `preco_mais_alto`              | Preço mais alto registrado de todos os tempos (All Time High).                                    | Float      |
| `ath_change_percentage`      | `queda_percentual_ath`         | Percentual de queda em relação ao valor mais alto de todos os tempos.                          | Float      |
| `ath_date`                   | `data_ath`                     | Data em que o valor mais alto foi registrado.                                                    | Data       |
| `atl`                        | `preco_mais_baixo`             | Preço mais baixo registrado de todos os tempos (All Time Low).                                     | Float      |
| `atl_change_percentage`      | `aumento_percentual_atl`       | Percentual de aumento em relação ao valor mais baixo de todos os tempos.                         | Float      |
| `atl_date`                   | `data_atl`                     | Data em que o valor mais baixo foi registrado.                                                   | Data       |
| `roi`                        | `retorno_investimento`         | Retorno sobre o investimento (caso aplicável).                                                  | Float      |
| `last_updated`               | `ultima_atualizacao`           | Data e hora da última atualização.                                                         | Data       |

