import seaborn as sns
import matplotlib.pyplot as plt

dots = sns.load_dataset('dots')
sns.relplot(
    data=dots, kind='line',
    x='time', y='firing_rate', col='align',
    hue='choice', size='coherence', style='choice',
    facet_kws=dict(sharex=False)
)
plt.show()