import pandas as pd
pd.set_option('display.width', None)

df = pd.read_csv('../dataframes/clientes_v2.csv')
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

print(df.head())


df.dropna(inplace=True)
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.nunique())
print(df.describe())

df = df[['idade', 'data', 'estado', 'salario', 'nivel_educacao', 'numero_filhos', 'estado_civil', 'area_atuacao']]
print(df.head())

df.to_csv('../dataframes/clientes_limpo_v2.csv')