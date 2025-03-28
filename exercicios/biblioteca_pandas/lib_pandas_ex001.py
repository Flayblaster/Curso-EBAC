import pandas as pd

#leitura do arquivo
arq = pd.read_csv("C:/Users/david/OneDrive/Documentos/Curso-EBAC/Curso-EBAC/exercicios/dataframes/vendas.csv")
df = pd.DataFrame(arq)

def ftm_total():
    #Definir as variaveis
    qtd = df['Quantidade']
    preco = df['Preço Unitário']
    
    #Fazer os calculos de faturamento por linha, faturamento total e criar uma nova coluna chamada faturamento
    ftm = qtd * preco
    df['Faturamento'] = ftm
    ftm_total = df['Faturamento'].sum()

    return ftm_total

def prdto_mais_vndo():
    #Localizacao do produto mais vendido 
    loc_prdto = df['Quantidade'].idxmax()
    
    prdto = df['Produto'][loc_prdto]
    return prdto

def ftm_por_catga():
    #Faturamento por categoria
    
    for categoria in df['Categoria'].unique():
        print(f'Categoria: {categoria} - Faturamento: ', end='')
        print(f"{df[df['Categoria'].str.contains(categoria)]['Faturamento'].sum():.2f}")
    
def cidade_com_mais_vendas():
    #Localizacao do produto mais vendido 
    loc_prdto = df['Quantidade'].idxmax()
    
    cidade = df['Cidade'][loc_prdto]
    return cidade


print('Faturamento total:', ftm_total())
print('Produto mais vendido:', prdto_mais_vndo())
print(f'Cidade onde teve mais vendas: {cidade_com_mais_vendas()}')
ftm_por_catga()
print('Itens mais vendidos em 02 de Fevereiro de 2024:')
print(df[df['Data'].str.contains('2024-02-01')]['Produto'])
