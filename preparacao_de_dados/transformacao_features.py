import pandas as pd
import numpy as np
from scipy import stats

pd.set_option('display.width', None)

df = pd.read_csv('../dataframes/clientes_limpo_v2.csv')
print(df.head())

#transformação logarítmica
df['salario_log'] = np.log1p(df['salario'])
print(df.head())

#transformação Box-Cox
df['salario-boxcox'], _ = stats.boxcox(df['salario'] + 1)
print(df.head())

#Codificação de frequência
estado_freq = df['estado'].value_counts() / len(df['estado'])
df['estado_freq'] = df['estado'].map(estado_freq)
print(df.head())

#interações
df['idade_filhos'] = df['idade'] * df['numero_filhos']
print(df.head())