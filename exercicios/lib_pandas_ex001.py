import pandas as pd

#leitura do arquivo
arq = pd.read_csv("C:/Users/david/OneDrive/Documentos/Curso-EBAC/Curso-EBAC/exercicios/vendas.csv")
df_vendas = pd.DataFrame(arq)

def fatu_total():
    qtd = df_vendas['Quantidade']
    preco = df_vendas['Preço Unitário']

    faturamento = qtd * preco
    df_vendas['Faturamento'] = faturamento
    faturamento_total = df_vendas['Faturamento'].sum()

    return faturamento_total

def mais_vend():
    id_mais_vendido = df_vendas['Quantidade'].idxmax()
    
    return df_vendas['Produto'][id_mais_vendido]


print('Faturamento total:', fatu_total())
print(df_vendas)
print(mais_vend())
print(df_vendas[['Categoria', 'Produto']])
