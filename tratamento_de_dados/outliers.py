import pandas as pd
from scipy import stats

pd.set_option('display.width', None)

df = pd.read_csv('./dataframes/clientes_limpo.csv')

df_filtro_basico = df[df['idade'] > 80]
print(df_filtro_basico[['nome', 'idade']])

# Identificar outliers com Z-score
z_scores = stats.zscore(df['idade'].dropna())
outliers_z = df[z_scores >= 1]
print('Outliers pelo Z-score:\n', outliers_z)

#identificar Outliers pelo IQR
q1 = df['idade'].quantile(0.25)
q3 = df['idade'].quantile(0.75)
IQR = q3 - q1
limite_baixo = q1 - 1.5 * IQR
limite_alto = q3 - 1.5 * IQR
print('Limites IQR:', limite_alto, limite_baixo)

df = df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_alto)]

#Filtrar endereçoes invalidos
df['endereco'] = df['endereco'].apply(lambda x: 'Endereço inválido' if len(x.split('\n')) < 3 else x)

#Tratar campos de texto
df['nome'] = df['nome'].apply(lambda x: 'Nome inválido' if isinstance(x, str) and len(x) > 50 else x)

df.to_csv('./dataframes/clientes_limpo_v1.2.csv', index=False)