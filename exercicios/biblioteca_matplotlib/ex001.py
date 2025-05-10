import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../dataframes/clima-basileia.csv')

pd.set_option('display.width', None)

df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

temp_media = dict()

for ind1, ind2 in zip(range(0, 43872, 24), range(24, 43872, 24)):
    media = (df['Temperature'][ind1:ind2].mean())
    mth = df['timestamp'][ind1].strftime('%Y-%m-%d')
    temp_media[mth] = media

fig, ax = plt.subplots()
ax.plot(temp_media.keys(), temp_media.values())
plt.show()