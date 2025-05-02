import pandas as pd

df = pd.read_csv('../dataframes/clientes.csv')

pd.set_option('display.width', None)

#Remover dados
#df.drop('pais', axis=1, inplace=True) #0 é linha e 1 é coluna
df.drop(2, axis=0, inplace=True)

#Normalizar campos de texto
prenome = ['srta', 'sra', 'sr', 'dra', 'ta', 'dr', '.']

df['nome'] = df['nome'].str.strip().str.lower()
for item in prenome:
    df['nome'] = df['nome'].str.replace(item, '')
df['estado'] = df['estado'].str.lower()
df['endereco'] = df['endereco'].str.lower()
df['estado'] = df['estado'].str.strip().str.upper()

#tratar valores nulos
df_fillna = df.fillna(0) #preenche valores nunlos com 0
df_dropna = df.dropna() #Remove registos nulos
df_dropna4 = df.dropna(thresh=4) #Mantem registos com no minimo 4 valores nao nulos
df = df.dropna(subset=['cpf']) #Remove nulos de um campo especifico

print('Valores nulos:', df.isnull().sum())
print('Valores nulos com fillna:', df_fillna.isnull().sum().sum())
print('valores nulos com dropna:', df_dropna.isnull().sum().sum())
print('Valores nulos com dropna4:', df_dropna4.isnull().sum().sum())
print('Valores nulos com CPF:', df.isnull().sum().sum())

df.fillna({'estado': 'Desconhecido'}, inplace=True)
df['endereco'] = df['endereco'].fillna('Endereco não informado')
df['idade_corrigida'] = df['idade'].fillna(df['idade'].mean())

#tratar formato de data
#df['data_corrigida'] = pd.to_datetime(df['data'], format='%Y/%m/%d', errors='coerce')

# Tratar duplicatas
print('Qtd de registros:', df.shape[0])
df.drop_duplicates()
df.drop_duplicates(subset='cpf', inplace=True)
print('Qtd de registro sem duplicatas: ', df.shape[0])

#salvar dataframe
df['idade'] = df['idade_corrigida']
df_salvar = df[['nome', 'cpf', 'idade', 'data', 'endereco', 'estado']]
df_salvar.to_csv('./dataframes/clientes_limpo_v1.1.csv', index=False)


