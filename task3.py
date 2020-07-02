import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv(r'tempYearly.csv')

sns.set(rc={'figure.figsize':(12,6)})
sns.scatterplot(x='Year',y='Temperature',data=df)
plt.show()

sns.set(rc={'figure.figsize':(12,6)})
sns.scatterplot(x='Rainfall',y='Temperature',data=df)
plt.show()