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
