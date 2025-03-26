import pandas as pd

#leitura do arquivo
arq = pd.read_csv("C:/Users/david/OneDrive/Documentos/Curso-EBAC/Curso-EBAC/exercicios/vendas.csv")
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

ftm_total()

def ftm_por_catga():
    #Faturamento por categoria
    
    for categoria in df['Categoria'].unique():
        print(f'Categoria: {categoria} - Faturamento: ', end='')
        print(f"{df[df['Categoria'].str.contains(categoria)]['Faturamento'].sum():.2f}")
    
ftm_por_catga()