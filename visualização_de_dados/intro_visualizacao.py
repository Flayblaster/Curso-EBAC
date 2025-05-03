import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

pd.set_option('display.width', None)

df = pd.read_csv('../dataframes/clientes_v3.csv')
print(df.head())
'''
#Histograma
plt.hist(df['salario'])

#Histograma - Parâmetros
plt.figure(figsize=(10, 6))
plt.hist(df['salario'], bins=100, color='green', alpha=0.8)
plt.title('Histograma - Distribuição de Salários')
plt.xlabel('Salário')
plt.ylabel('Frequência')
plt.xticks(ticks=range(0, int(df['salario'].max())+2000, 2000))
plt.grid(True)
'''

#Multiplus gráficos
plt.figure(figsize=(10, 6))
plt.subplot(2, 2, 1)
plt.scatter(df['salario'], df['anos_experiencia'], color='#ff7088', alpha=0.3, s=20)
plt.title('Dispersão - Salário x Experiência')
plt.xlabel('Salário')
plt.ylabel('Experiência')

plt.subplot(2, 2, 2)
plt.bar(df['numero_filhos'], df['idade'])
plt.title('Dispersão - Idade x Filhos')
plt.xlabel('Idade')
plt.ylabel('Filhos')


plt.subplot(2, 2, 3)
corr = df['salario_log'] * df['idadeMinMaxScaler']
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlação Salário e Idade')

plt.show()