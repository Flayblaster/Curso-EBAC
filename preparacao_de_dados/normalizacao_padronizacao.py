import pandas as pd
from sklearn.preprocessing import RobustScaler, MinMaxScaler, StandardScaler

pd.set_option('display.width', None)

df = pd.read_csv('../dataframes/clientes_limpo_v2.csv')

print(df.head())

df = df[['idade', 'salario']]

#Normalizacao - Ele deixa os valores numa mesma escala
scaler = MinMaxScaler()
df['idadeMinMaxScaler'] = scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler'] = scaler.fit_transform(df[['salario']])

scaler = MinMaxScaler(feature_range=(-1, 1)) #feature_range - Coloca um limite para a normalização
df['idadeMinMaxScaler_mm'] = scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler_mm'] = scaler.fit_transform(df[['idade']])

#Padronizacao - faz a padronização dos dados, colocando eles num intervalo de 0 e 1. Os valores tendem a ter a media 0 e desvio padrao 1
scaler = StandardScaler()
df['idadeStandardScaler'] = scaler.fit_transform(df[['idade']])
df['salarioStandardScaler'] = scaler.fit_transform(df[['salario']])

#Padronizacao - RobustScaler - Os valores usam a mediana e o como desvio padrao o IQR
scaler = RobustScaler()
df['idadeRobustScaler'] = scaler.fit_transform(df[['idade']])
df['salarioRobustScaler'] = scaler.fit_transform(df[['salario']])

