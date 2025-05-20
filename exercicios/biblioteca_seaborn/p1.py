import pandas as pd

df = pd.read_csv('/Curso-EBAC/exercicios/dataframes/flights.csv')

pd.set_option('display.width', None)

#Normalizar campos de texto
def normalizar_campo(dataf, coluna):
    dataf[coluna] = dataf[coluna].astype(str)
    dataf[coluna] = dataf[coluna].str.strip().str.lower()
    return dataf

#Tratar valores nulos
def treat_nan(dataf, f_or_r):
    if 'f' in f_or_r:
        dataf.fillna(0, inplace=True)
    else:
        dataf.dropna(inplace=True)
    return dataf

#Tratamento especifico para datas desse dataframe
df['datac'] = df['year'].astype(str) + '-' + df['month'].astype(str) + '-' + '01'

#Tratar duplicadas
def treat_duplicates(dataf):
    dataf.drop_duplicates(inplace=True)
    return dataf

#Salvar dataframe
def save(dataf, name):
    dataf.to_csv(f'C:/Users/david/OneDrive/Documentos/Curso-EBAC/Curso-EBAC/exercicios/dataframes/{name + '_treat'}.csv', index=False)

df = normalizar_campo(df, 'month')
df = normalizar_campo(df, 'year')
df = treat_nan(df, 'fill')
df = treat_duplicates(df)
print(df)
save(df, 'flights')

print(df)