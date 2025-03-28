import pandas as pd

df = pd.read_csv('C:/Users/david/OneDrive/Documentos/Curso-EBAC/Curso-EBAC/exercicios/dataframes/dados_funcionarios.csv')


def media_salarial():
    soma = df["Salário"].sum()
    contagem = df["ID"].count()
    media = soma/contagem

    return f'{media:.2f}'

def cinco_maiores():
    df_sorted = df.sort_values(by=['Salário'], ascending=False)

    return df_sorted[['Nome', 'Salário']].head(5)

def qtd_por_depart():
    departs = df['Departamento'].unique()
    departamentos = pd.DataFrame(columns=['Departamentos', 'Qtd_de_Pessoas'])
    departamentos['Departamentos'] = departs
    
    for depart in departs:
        count = df['Departamento'].loc[df['Departamento'] == depart].count()
        departamentos.loc[departamentos['Departamentos'] == depart, ['Qtd_de_Pessoas']] = count
    
    return departamentos

def sal_acima_media():
    media_sal = df['Salário'].mean()
    acima_media = df.loc[df['Salário'] >= media_sal, ['Nome', 'Salário']]

    return acima_media.sort_values(by=['Salário'], ascending=False)

def media_sal_depart():
    df_media = qtd_por_depart()
    
    for depart in df['Departamento'].unique():
       media = df[df['Departamento'] == depart]['Salário'].mean()
       df_media.loc[df['Departamento'] == depart, 'Media_por_Departamento'] = media
       df_media.sort_values(by='Media_por_Departamento', ascending=False, inplace=True) 

    return df_media[['Departamentos', 'Media_por_Departamento']]

def funci_antigo():
    antigao = df['Data_Admissao'].min()
    antigasso = df.loc[df['Data_Admissao'] == antigao]
    return antigasso

print(f'Média salarial: {media_salarial()}\n')
print(f'Cinco maiores salários:\n{cinco_maiores()}\n')
print(f'Quantidade de pessoas por departamento:\n{qtd_por_depart()}\n')
print(f'Funcionários que recebem um salário acima da média ({media_salarial()}):\n{sal_acima_media()}\n')
print(f'Media salarial por departamento:\n{media_sal_depart()}\n')
print(f'Funcionário mais antigo:\n{funci_antigo()}')
