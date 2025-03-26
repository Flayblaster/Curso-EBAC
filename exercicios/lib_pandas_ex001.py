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

def fat_por_cat():
    counte = eletronicos_total = moveis_total = 0
    for itens in df_vendas.Categoria:
        if 'Eletr' in itens:
            eletronicos_total += df_vendas.iloc[counte, 6]
        elif 'Móveis' in itens:
            moveis_total += df_vendas.iloc[counte, 6]
        counte += 1
    return (moveis_total, eletronicos_total)

def cid_mais_vendas():
    id_mais_vendido = df_vendas['Quantidade'].idxmax()
    
    return df_vendas['Cidade'][id_mais_vendido]

print('Faturamento total:', fatu_total())
print('Objeto mais vendido:', mais_vend())
print(f'Cidade onde teve mais vendas: {cid_mais_vendas()}')
print(f'Faturamento por categoria:\n',
      f'-Eletrônicos: {fat_por_cat()[1]}\n' ,
      f'-Móveis: {fat_por_cat()[0]}')


#df_vendas['Data'] = pd.to_datetime(df_vendas['Data'])

print('Itens mais vendidos em 02 de Fevereiro de 2024:')
print(df_vendas[df_vendas['Data'].str.contains('2024-02-01')]['Produto'])
