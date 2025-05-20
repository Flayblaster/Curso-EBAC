import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
import pandas as pd
from seaborn import load_dataset

df_fly = pd.read_csv('../dataframes/flights.csv')
df_planet = pd.read_csv('../dataframes/planets.csv')
df_co2 = pd.read_csv('../dataframes/co2_emissions.csv')

fig, axes = plt.subplots(2, 2)

#subplot 1
flight = df_fly.pivot(columns='month', index='year', values='passengers')
sns.heatmap(flight)

#subplot 2
planets = sns.load_dataset('planets').dropna()
sns.violinplot(data=planets, x='method', y='distance',
              split=True, inner="quart", hue='number', ax=axes[0,1])

plt.show()