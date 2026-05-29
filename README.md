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
* numpy
* time
* os
* csv
* matplotlib

---

# Arquitetura do Projeto

# 2. Ambiente Experimental

| Item                        | Descrição                  |
| --------------------------- | -------------------------- |
| Processador                 | Intel Core i7-13000H       |
| Número de núcleos           | 7 Cores / 12 Threads       |
| Memória RAM                 | 16GB DDR4                  |
| Sistema Operacional         | Windows 11                 |
| Linguagem utilizada         | Python                     |
| Biblioteca de paralelização | MPI4Py                     |
| Ambiente de execução        | VSCode                     |
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

Gráfico de Tempo de Execução
![Gráfico Tempo Execução](tempo_execucao.png)

---

# 8. Gráfico de Speedup
![Gráfico Speedup](speedup.png)

---

# 9. Gráfico de Eficiência
![Gráfico Eficiência](eficiencia.png)

---

# Benchmark

O projeto também permite comparar diferentes quantidades de processos. (só exemplo)

| Processos | Tempo (s) | Speedup | Eficiência |
| --------- | --------- | ------- | ---------- |
| 1         | 381,32    | 1.0     | 100%       |
| 2         | 189,85    | 2.01    | 100,43%    |
| 4         | 89,63     | 4.25    | 106,36%    |
| 8         | 57,37     | 6.65    | 83,08%     |
| 12        | 50,71     | 7.52    | 62,66%     |

---

# Conceitos Envolvidos

O projeto aborda diversos conceitos importantes:

* Programação concorrente
* Paralelismo
* Processamento massivo de dados
* Escalabilidade
* Benchmarking
* Big Data
* Análises pessoais
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
