# Desafio Final: Análise Financeira com Python 📊

Este projeto resolve o desafio final do módulo de Python focado em Análise de Dados da ClearBank. O objetivo é processar um arquivo CSV com transações financeiras, limpar dados corrompidos, gerar métricas e exportar resultados.

## 📁 Estrutura do Projeto

- `desafio-final.ipynb`: Notebook Jupyter principal contendo a solução nativa Python (leitura, validação, relatório e gráfico opcional do Matplotlib).
- `analise_pandas.py`: Script Python isolado contendo o Requisito Opcional 1 (agrupamento via pandas).
- `transacoes.csv`: Base de dados de teste (gerada pela Célula 1 do notebook).
- `relatorio.json`: Saída processada contendo o resumo financeiro mensal gerado pelo código.
- `grafico.png`: Requisito Opcional 2 gerado pelo Matplotlib mostrando os saldos.

## 🚀 Como Executar

1. Abra o arquivo `desafio-final.ipynb` no VS Code (com a extensão Jupyter instalada) ou no Google Colab.
2. Execute a **Célula 1** para gerar a massa de dados (`transacoes.csv`).
3. Execute as **Células 2 e 3** em sequência. A Célula 3 é a Célula Principal que orquestra tudo e imprimirá o relatório visual no terminal, além de criar o `relatorio.json`.
4. Execute a **Célula 4** para gerar o gráfico de barras salvando-o como `grafico.png`.
5. Para testar o Pandas, basta rodar o comando `python analise_pandas.py` em seu terminal local.

## 📦 O Que o Notebook Gera Como Saída

Ao executar o notebook por completo, as seguintes saídas são geradas automaticamente pelo código:

* **Relatório no Terminal (Console):** Uma exibição visualmente formatada contendo o resumo mensal financeiro (total de transações válidas e inválidas, soma de créditos e débitos, saldos, médias e extremos) e uma seção de alerta listando transações consideradas suspeitas (acima de R$ 10.000,00).
* **Arquivo `relatorio.json`:** Um arquivo de dados estruturado exportando as métricas consolidadas do período, pronto para integração com outros sistemas ou APIs.
* **Arquivo `grafico.png`:** *(Referente ao Requisito Opcional)* Uma imagem em alta qualidade gerada via Matplotlib, contendo um gráfico de barras que ilustra a evolução do saldo financeiro mês a mês.
* **Arquivo `transacoes.csv`:** O próprio dataset inicial é gerado como saída na primeira célula do código para garantir a reprodutibilidade dos testes.
