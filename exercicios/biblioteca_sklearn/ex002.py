import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.width', None)

# Definindo alguns produtos para variar os preços
produtos = ['Camiseta', 'Calça Jeans', 'Tênis Esportivo', 'Livro', 'Smartphone']

# Criando datas aleatórias dentro de um período
def criar_datas(num_linhas, inicio='2024-01-01', fim='2024-12-31'):
    datas = pd.to_datetime(np.random.uniform(pd.to_datetime(inicio).value,
                                             pd.to_datetime(fim).value, num_linhas)).strftime('%Y-%m-%d')
    return datas

# Gerando dados com alguns outliers intencionais
np.random.seed(42) # Para reprodutibilidade
num_linhas = 100
data = {
    'id_transacao': range(1, num_linhas + 1),
    'produto': np.random.choice(produtos, num_linhas),
    'quantidade': np.random.randint(1, 10, num_linhas),
    'preco_unitario': np.random.uniform(10, 200, num_linhas),
    'data_venda': criar_datas(num_linhas)
}
df_vendas = pd.DataFrame(data)

# Calculando o valor total
df_vendas['valor_total'] = df_vendas['quantidade'] * df_vendas['preco_unitario']

# Introduzindo alguns outliers de forma manual
df_vendas.loc[5, 'quantidade'] = 50  # Venda de alta quantidade
df_vendas.loc[15, 'preco_unitario'] = 5   # Preço unitário muito baixo
df_vendas.loc[30, 'valor_total'] = 5000  # Valor total muito alto (erro de digitação?)
df_vendas.loc[70, 'quantidade'] = 1
df_vendas.loc[70, 'preco_unitario'] = 1000 # Preço unitário muito alto

# Garantindo que o valor total seja recalculado após as alterações manuais
df_vendas['valor_total'] = df_vendas['quantidade'] * df_vendas['preco_unitario']
print(df_vendas)

colunas_numericas = df_vendas.select_dtypes(include=np.number).columns
print('Colunas numéricas:', list(colunas_numericas))

Q1 = df_vendas['valor_total'].quantile(0.25)
Q3 = df_vendas['valor_total'].quantile(0.75)
iqr = Q3 - Q1

limite_inferior = (Q1 - 1.5*iqr)
limite_superior = (Q3 - 1.5*iqr)

df_vendas['outliers_iqr'] = df_vendas['valor_total'].apply(lambda x: 0 if limite_inferior >= x <= limite_superior else 1)

x = list(df_vendas['outliers_iqr'])
y = list(df_vendas['outliers_iqr'])

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
