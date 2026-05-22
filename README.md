# programa-o_concorrente_de_avaliação_da_steam
# Processamento Concorrente de Avaliações da Steam em Larga Escala

## Descrição do Projeto

Este projeto tem como objetivo realizar o processamento concorrente de avaliações da plataforma Steam em larga escala, permitindo identificar padrões de satisfação e insatisfação dos jogadores por meio da análise de grandes volumes de dados.

A proposta combina técnicas de:

* Programação concorrente
* Paralelismo
* Processamento de dados
* Análise de sentimentos
* Manipulação de arquivos massivos
* Benchmarking de desempenho

O sistema foi desenvolvido com foco em desempenho, escalabilidade e eficiência computacional, utilizando múltiplas threads/processos para acelerar o processamento das avaliações.

---

# Objetivos

## Objetivo Geral

Desenvolver uma aplicação capaz de processar milhares ou milhões de avaliações da Steam de forma concorrente, reduzindo o tempo de execução e permitindo a extração de informações relevantes sobre a experiência dos jogadores.

## Objetivos Específicos

* Ler arquivos massivos contendo avaliações.
* Processar avaliações simultaneamente.
* Identificar padrões de satisfação e insatisfação.
* Realizar análise estatística das avaliações.
* Comparar desempenho serial vs concorrente.
* Medir speedup e eficiência.
* Avaliar escalabilidade do sistema.

---

# Problema Resolvido

O processamento de grandes volumes de avaliações de usuários pode se tornar extremamente lento em execução sequencial.

Com técnicas de concorrência e paralelismo, o sistema distribui a carga de trabalho entre múltiplos núcleos do processador, reduzindo significativamente o tempo de processamento.

Isso permite:

* Processar datasets massivos.
* Melhorar desempenho computacional.
* Tornar a análise viável em larga escala.
* Simular cenários reais de Big Data.

---

# Tecnologias Utilizadas

## Linguagem

* Python 3

## Bibliotecas

* multiprocessing
* concurrent.futures
* pandas
* numpy
* time
* os
* csv
* matplotlib

---

# Arquitetura do Projeto

O sistema é dividido em etapas:

## 1. Leitura do Dataset

Os arquivos contendo avaliações da Steam são carregados para memória.

## 2. Divisão de Tarefas

O dataset é dividido em blocos menores.

## 3. Processamento Concorrente

Cada processo/thread trabalha em uma parte do dataset simultaneamente.

## 4. Análise das Avaliações

O sistema identifica:

* Avaliações positivas
* Avaliações negativas
* Frequência de palavras
* Padrões de comportamento
* Tendências de satisfação

## 5. Consolidação dos Resultados

Os resultados processados são reunidos em uma saída final.

---

# Concorrência e Paralelismo

O projeto utiliza processamento concorrente para melhorar desempenho.

## Estratégias Utilizadas

### Multiprocessing

Utiliza múltiplos processos independentes para aproveitar múltiplos núcleos da CPU.

### Execução Paralela

Cada worker processa avaliações simultaneamente.

---

# Métricas Avaliadas

O sistema realiza benchmarking de desempenho.

## Métricas

* Tempo de execução
* Speedup
* Eficiência
* Escalabilidade
* Uso de CPU
* Ganho de desempenho

## Fórmula de Speedup

```math
S = rac{T_{serial}}{T_{paralelo}}
```

Onde:

* S = Speedup
* Tserial = tempo serial
* Tparalelo = tempo paralelo

## Fórmula de Eficiência

```math
E = rac{S}{P}
```

Onde:

* E = Eficiência
* P = número de processos/threads

---
# Resultados Esperados

Com o uso de concorrência, espera-se:

* Redução significativa do tempo de execução.
* Melhor aproveitamento da CPU.
* Escalabilidade para datasets maiores.
* Melhor desempenho comparado ao processamento serial.

---

# Benchmark

O projeto também permite comparar diferentes quantidades de processos. (só exemplo)

| Processos | Tempo (s) | Speedup | Eficiência |
| --------- | --------- | ------- | ---------- |
| 1         | 120       | 1.0     | 100%       |
| 2         | 70        | 1.71    | 85%        |
| 4         | 38        | 3.15    | 78%        |
| 8         | 22        | 5.45    | 68%        |

---

# Possíveis Melhorias Futuras

* Implementar análise de sentimentos com IA.
* Utilizar processamento distribuído.
* Criar dashboard web.
* Adicionar visualização gráfica em tempo real.
* Implementar filas de processamento.
* Adicionar banco de dados para persistência.
* Utilizar Apache Spark.

---

# Conceitos Envolvidos

O projeto aborda diversos conceitos importantes:

* Programação concorrente
* Paralelismo
* Processamento massivo de dados
* Escalabilidade
* Benchmarking
* Big Data
* Análise de sentimentos
* Processamento de linguagem natural
* Threads e processos
* Balanceamento de carga

---

# Aplicações Reais

Este tipo de solução pode ser utilizado em:

* Plataformas de jogos
* Redes sociais
* Sistemas de recomendação
* Marketplaces
* Sistemas de feedback
* Análise de opinião pública
* Plataformas de streaming

---

# Conclusão

O projeto demonstra como técnicas de concorrência e paralelismo podem aumentar significativamente o desempenho de aplicações que processam grandes volumes de dados.

Além disso, o sistema mostra na prática como a computação paralela pode ser aplicada em cenários reais de análise de avaliações e mineração de dados.

---

Este projeto é livre para estudos e fins acadêmicos.
