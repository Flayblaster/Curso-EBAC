import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

pd.set_option('display.width', None)

df = pd.read_csv('../dataframes/clientes_v3.csv')
print(df.head().to_string())

#Histogram
plt.hist(df['salario'])
#plt.show()

#Histogram - Parameters
plt.figure(figsize=(10, 6))
plt.hist(df['salario'], bins=100, color='pink', alpha=1)
plt.title('Histogram - Salaries Distribution')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.xticks(ticks=range(0, int(df['salario'].max())+2000, 2000))
plt.grid(True)
#plt.show()

#Multy graphics
plt.figure(figsize=(10, 6))

#Scatter graphic
plt.subplot(2, 2, 1) #2 linhas, 2 colunas, 2 grafico
plt.scatter(df['salario'], df['salario'], color='pink')
plt.title('Scatter - Salary and Salary')
plt.xlabel('Salary')
plt.ylabel('Salary')

#Scatter graphic
plt.subplot(1, 2, 2)
plt.scatter(df['salario'], df['anos_experiencia'], color='pink', alpha=0.6, s=30)
plt.title('Scatter - Salary and Tenure')
plt.xlabel('Salary')
plt.ylabel('Tenure')

#Heat map
corr = df[['salario', 'anos_experiencia']].corr()
plt.subplot(2, 2, 3)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlação Salário e Idade')

plt.tight_layout()
plt.show()