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
5. Para testar o Pandas, basta rodar o comando `python analise_pandas.py` em seu terminal.
