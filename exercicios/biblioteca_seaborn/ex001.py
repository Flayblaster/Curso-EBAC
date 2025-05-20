# Import seaborn
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df_fly = sns.load_dataset('planets')
df_fly.to_csv('../dataframes/planets.csv')