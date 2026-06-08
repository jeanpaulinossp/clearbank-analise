import pandas as pd

def executar_analise_pandas():
    print("Executando leitura e agrupamento via Pandas...")
    try:
        df = pd.read_csv("transacoes.csv")
        
        df = df.dropna(subset=['id', 'cliente_id', 'data', 'tipo', 'valor'])
        df['valor'] = pd.to_numeric(df['valor'], errors='coerce')
        df = df[(df['valor'] > 0) & (df['tipo'].isin(['credito', 'debito']))]
        df['data'] = pd.to_datetime(df['data'], errors='coerce')
        df = df.dropna(subset=['data', 'valor'])
        
        df['mes'] = df['data'].dt.to_period('M')
        
        resumo = df.groupby('mes').apply(lambda x: pd.Series({
            'Transações': x['id'].count(),
            'Total Crédito': x.loc[x['tipo'] == 'credito', 'valor'].sum(),
            'Total Débito': x.loc[x['tipo'] == 'debito', 'valor'].sum()
        })).reset_index()
        
        resumo['Saldo'] = resumo['Total Crédito'] - resumo['Total Débito']
        print("\nResultado da Análise com Pandas (deve bater com a versão nativa):")
        print(resumo.to_string(index=False))
        
    except FileNotFoundError:
        print("Arquivo transacoes.csv não encontrado.")

if __name__ == "__main__":
    executar_analise_pandas()