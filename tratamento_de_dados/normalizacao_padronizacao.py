import pandas as pd
from sklearn.preprocessing import RobustScaler, MinMaxScaler, StandardScaler

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('./dataframes/clientes_v2.csv')
df = df[['idade', 'salario']]

#Normalização - MinMaxScaler
scaler = MinMaxScaler()
df['idadeMMS'] = scaler.fit_transform(df[['idade']])
df['salarioMMS'] = scaler.fit_transform(df[['salario']])

MMS = MinMaxScaler(feature_range=(-1, 1))
df['idadeMMS_mm'] = MMS.fit_transform(df[['idade']])
df['salarioMMS_mm'] = MMS.fit_transform(df[['salario']])

print(df.head())