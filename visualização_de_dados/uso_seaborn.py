import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('../dataframes/clientes_v3.csv')

#Pairplot graphic
sns.pairplot(df[['idade', 'salario', 'anos_experiencia', 'nivel_educacao']])
plt.show()

#Regression graphic
sns.regplot(x='idade', y='salario', data=df, scatter_kws={'alpha': 0.5, 'color':'#34c289'})
plt.title('Regressão de Salário por idade')
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.show()

sns.countplot(x='estado_civil', hue='nivel_educacao', data=df, palette='pastel')
plt.xlabel('Estado civil')
plt.ylabel('Quantidade Clientes')
plt.legend(title='Nível de Educação')
plt.show()