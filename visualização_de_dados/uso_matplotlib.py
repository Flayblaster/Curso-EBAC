import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('../dataframes/clientes_v3.csv')
print(df.head().to_string())

#Bar graphic
plt.figure(figsize=(10, 6))
education_count = df['nivel_educacao'].value_counts()
level_of_scholarity = df['nivel_educacao'].unique()
plt.bar(x=level_of_scholarity, height=education_count, color='blue')
plt.title('Scholarity Level')
plt.xlabel('Education Levels')
plt.ylabel('Amount of People')
plt.xticks(rotation=0) #Rotacao do texto
plt.show()

#Pizza graphic
plt.figure(figsize=(10, 6))
plt.pie(education_count, labels=level_of_scholarity, autopct='%.1f%%', startangle=90)
plt.title('Distribuição de Nível de Educação')
plt.show()

#Hexbin
plt.hexbin(df['idade'], df['salario'], gridsize=40, cmap='Blues')
plt.colorbar(label='Contagem dentro do bin')
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.title('Dispersão de Idade e Salário')
plt.show()

#Make a pizza graphic
plt.figure(figsize=(8, 8))