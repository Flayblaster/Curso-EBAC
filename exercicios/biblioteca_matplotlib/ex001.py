import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../dataframes/clima-basileia.csv')

pd.set_option('display.width', None)

print(df.head(20))
print(df.info())
print(df.describe)