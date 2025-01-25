# Dicionário de Dados do Output do Endpoint da CoinGecko

Este documento descreve os campos retornados pelo endpoint da CoinGecko utilizado para listar as 100 principais criptomoedas por valor de mercado: `https://api.coingecko.com/api/v3/coins/markets`. O objetivo é fornecer uma visão clara e organizada dos dados disponíveis, detalhando cada campo com sua descrição, tipo de dado e uma sugestão de nome traduzido para uso em bancos de dados. Isso garante consistência e padronização no tratamento dessas informações em seu projeto.

| Campo                        | Descrição                                                                                         | Tipo       | Sugestão de Coluna Traduzida    |
|------------------------------|-------------------------------------------------------------------------------------------------|------------|---------------------------------|
| `id`                         | Identificador único da criptomoeda.                                                             | String     | id                              |
| `symbol`                     | Símbolo ou ticker da criptomoeda (ex.: "BTC").                                                  | String     | simbolo                         |
| `name`                       | Nome completo da criptomoeda (ex.: "Bitcoin").                                                  | String     | nome                            |
| `image`                      | URL da imagem associada à criptomoeda.                                                          | String     | imagem                          |
| `current_price`              | Preço atual da criptomoeda na moeda base (ex.: USD, BRL).                                        | Float      | preco_atual                     |
| `market_cap`                 | Valor total de mercado da criptomoeda.                                                          | Float      | valor_mercado                   |
| `market_cap_rank`            | Posição da criptomoeda no ranking de mercado.                                                   | Inteiro    | ranking_mercado                 |
| `fully_diluted_valuation`    | Valorização máxima com base no fornecimento máximo de moedas.                                    | Float      | valorizacao_diluida_total       |
| `total_volume`               | Volume total negociado nas últimas 24 horas.                                                   | Float      | volume_total                    |
| `high_24h`                   | Maior preço da criptomoeda nas últimas 24 horas.                                              | Float      | maior_preco_24h                 |
| `low_24h`                    | Menor preço da criptomoeda nas últimas 24 horas.                                              | Float      | menor_preco_24h                 |
| `price_change_24h`           | Variação absoluta no preço nas últimas 24 horas.                                        | Float      | variacao_preco_24h              |
| `price_change_percentage_24h`| Percentual de variação do preço nas últimas 24 horas.                                      | Float      | variacao_percentual_24h         |
| `market_cap_change_24h`      | Mudança no valor de mercado absoluto nas últimas 24 horas.                                     | Float      | mudanca_valor_mercado_24h       |
| `market_cap_change_percentage_24h`| Percentual de mudança no valor de mercado nas últimas 24 horas.                              | Float      | mudanca_percentual_mercado_24h  |
| `circulating_supply`         | Quantidade de moedas em circulação.                                                            | Float      | quantidade_circulacao           |
| `total_supply`               | Quantidade total de moedas emitidas.                                                             | Float      | quantidade_total                |
| `max_supply`                 | Quantidade máxima de moedas planejadas.                                                         | Float      | quantidade_maxima               |
| `ath`                        | Preço mais alto registrado de todos os tempos (All Time High).                                    | Float      | preco_mais_alto                 |
| `ath_change_percentage`      | Percentual de queda em relação ao valor mais alto de todos os tempos.                          | Float      | queda_percentual_ath            |
| `ath_date`                   | Data em que o valor mais alto foi registrado.                                                    | Data       | data_ath                        |
| `atl`                        | Preço mais baixo registrado de todos os tempos (All Time Low).                                     | Float      | preco_mais_baixo                |
| `atl_change_percentage`      | Percentual de aumento em relação ao valor mais baixo de todos os tempos.                         | Float      | aumento_percentual_atl          |
| `atl_date`                   | Data em que o valor mais baixo foi registrado.                                                   | Data       | data_atl                        |
| `roi`                        | Retorno sobre o investimento (caso aplicável).                                                  | Float      | retorno_investimento            |
| `last_updated`               | Data e hora da última atualização.                                                         | Data       | ultima_atualizacao              |

