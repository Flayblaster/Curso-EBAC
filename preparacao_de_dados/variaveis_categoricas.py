import pandas as pd
from sklearn.preprocessing import LabelEncoder

pd.set_option('display.width', None)

df = pd.read_csv('../dataframes/clientes_limpo_v2.csv')

#Codificação one-hot para 'estado-civil'
df = pd.concat([df, pd.get_dummies(df['estado_civil'], prefix='estado_civil')], axis=1)
print(df.head())

#Codificação ordinal para 'nivel_educacao'
educacao_ordem = {'Ensino Fundamental': 1, 'Ensino Médio': 2, 'Ensino Superior': 3, 'Pós-graduação': 4}
df['nivel-educacao-ordinal'] = df['nivel_educacao'].map(educacao_ordem)
print(df.head())

#Codificação através do cat.codes
df['area_atuacao_cod'] = df['area_atuacao'].astype('category').cat.codes
print(df.head())

#label encoder converte cada valor unico em nnumeros de 0 a n_classes-1
labelencoder = LabelEncoder()
df['estado_cod'] = labelencoder.fit_transform(df['estado'])
print(df.head())