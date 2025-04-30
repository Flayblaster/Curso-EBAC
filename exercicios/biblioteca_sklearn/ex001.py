import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import numpy as np

pd.set_option('display.width', None)

# 1. Criando um DataFrame de exemplo
data = {
    'idade': [25, 40, 32, 68, 51, 38, 29, 45],
    'peso': [65, 80, 72, 95, 78, 68, 55, 88],
    'altura': [170, 185, 168, 175, 180, 172, 165, 190],
    'pressao_sistolica': [120, 135, 128, 145, 130, 125, 118, 140],
    'pressao_diastolica': [80, 85, 82, 90, 84, 81, 78, 88],
    'nivel_glicose': [90, 110, 95, 130, 105, 98, 85, 115],
    'fumante': ['Não', 'Sim', 'Não', 'Sim', 'Não', 'Não', 'Não', 'Sim'],
    'atividade_fisica': ['Baixa', 'Alta', 'Moderada', 'Baixa', 'Alta', 'Moderada', 'Baixa', 'Alta']
}
df_pacientes = pd.DataFrame(data)

print('DataFrame original: ')
print(df_pacientes)
print('\n', '='*100, '\n')

# 2. Identificando as colunas numéricas
colunas_numericas = df_pacientes.select_dtypes(include=np.number).columns

print('Colunas Numérica Identificadas:', list(colunas_numericas))
print('\n', '='*100, '\n')

# 3. Padronizando as colunas numéricas usando StandardScaler
scaler_padronizado = StandardScaler()
dados_padronizados = scaler_padronizado.fit_transform(df_pacientes[colunas_numericas])

# 4. Criando um DataFrame com os dados padronizados
df_padronizado = pd.DataFrame(dados_padronizados, columns=colunas_numericas)

# 5. Adicionando as colunas categóricas de volta
df_padronizado[['fumante', 'atividade_fisica']] = df_pacientes[['fumante', 'atividade_fisica']]

print('DataFrame Padronizado (StandardScaler):')
print(df_padronizado)
print('\n', '='*100, '\n')

# 6. Normalizando as colunas numericas usando MinMaxScaler
scaler_normalizacao = MinMaxScaler()
dados_normalizados = scaler_normalizacao.fit_transform(df_pacientes[colunas_numericas])

# 7. Criando um DataFrame com os dados normalizados
df_normalizado = pd.DataFrame(dados_normalizados, columns=colunas_numericas)

# 8. Adicionando as colunas categoricas de volta
df_normalizado[['fumante', 'atividade_fisica']] = df_pacientes[['fumante', 'atividade_fisica']]

print('DataFrame Normalizado (MinMaxScaler):')
print(df_normalizado)
print('\n', '='*100, '\n')

# 9. Comparando as estatísticas descritivas
print('Estatísticas Descritivas do DataFrame Original (Colunas Numéricas):')
print(df_pacientes[colunas_numericas].describe())
print('\n', '='*100, '\n')

print('Estatisticas Descritivas do DataFrame Padronizado (Colunas Numéricas):')
print(df_padronizado[colunas_numericas].describe())
print('\n', '='*100, '\n')

print('Estatística Descritivas do DataFrame Normalizado (Colunas Numéricas):')
print(df_normalizado[colunas_numericas].describe())
