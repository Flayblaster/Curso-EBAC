import pandas as pd

df = pd.read_csv('C:/Users/david/OneDrive/Documentos/Curso-EBAC/Curso-EBAC/exercicios/dataframes/dados_funcionarios.csv')


def media_salarial():
    """
    Cálcula a média salarial dos funcionários
    soma - faz a soma dos salários
    contagem - conta quantos funcionários existem
    media - divide a soma pela contagem
    """

    soma = df["Salário"].sum()
    contagem = df["ID"].count()
    media = soma/contagem

    return f'{media:.2f}'

def cinco_maiores():
    """
    Encontra o cinco maiores salarios
    df_sorted - organiza o df principal com base no salário, do maior pro menor
    df_head - escolhe os cinco primeiros do df_sorted
    """

    df_sorted = df.sort_values(by=['Salário'], ascending=False)
    df_head = df_sorted[['Nome', 'Salário']].head(5)

    return df_head

def qtd_por_depart():
    """
    Conta quantos funcionários existem por departamento
    departs - gera uma lista com os departamentos
    departamentos - é um df que organiza as informações em Departaemntos e Qtd_de_Pessoas
    for - itera os departamentos
    count - conta quantas pessoas tem naquele departamento
    """
    
    departs = df['Departamento'].unique()
    departamentos = pd.DataFrame(columns=['Departamentos', 'Qtd_de_Pessoas'])
    departamentos['Departamentos'] = departs
    
    for depart in departs:
        count = df['Departamento'].loc[df['Departamento'] == depart].count()
        departamentos.loc[departamentos['Departamentos'] == depart, ['Qtd_de_Pessoas']] = count
    
    return departamentos

def sal_acima_media():
    """
    Calcula a média salarial e mostra todos os salários acima da média
    media_sal - média dos salários
    acima_media - acha os salários acima da média
    media_sorted - organiza os salários do maior pro menor
    """
    
    media_sal = df['Salário'].mean()
    acima_media = df.loc[df['Salário'] >= media_sal, ['Nome', 'Salário']]
    media_sorted = acima_media.sort_values(by=['Salário'], ascending=False)
    
    return media_sorted

def media_sal_depart():
    """
    Cálcula a média salarial por departamento
    df_media - usa o df da funcao qtd_por_depart() para adcionar uma coluna com as medias salarial dos departamentos
    media - acha a média dos salarios
    Dps é criado um nova coluna chamada Media_por_Departamento
    """

    df_media = qtd_por_depart()
    
    for depart in df['Departamento'].unique():
       media = df[df['Departamento'] == depart]['Salário'].mean()
       df_media.loc[df['Departamento'] == depart, 'Media_por_Departamento'] = media
       df_media.sort_values(by='Media_por_Departamento', ascending=False, inplace=True) 

    return df_media[['Departamentos', 'Media_por_Departamento']]

def funci_antigo():
    """
    acha o funcionário com mais tempo na empresa
    antigao  - acha o menor valor da data de admissao
    antigasso - pega a linha que pertece aquele valor de data 
    """
    antigao = df['Data_Admissao'].min()
    antigasso = df.loc[df['Data_Admissao'] == antigao]
    return antigasso

print(f'Média salarial: {media_salarial()}\n')
print(f'Cinco maiores salários:\n{cinco_maiores()}\n')
print(f'Quantidade de pessoas por departamento:\n{qtd_por_depart()}\n')
print(f'Funcionários que recebem um salário acima da média ({media_salarial()}):\n{sal_acima_media()}\n')
print(f'Media salarial por departamento:\n{media_sal_depart()}\n')
print(f'Funcionário mais antigo:\n{funci_antigo()}')
