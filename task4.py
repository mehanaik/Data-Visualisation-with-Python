import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv(r'./birthYearly.csv')
print(data)

dataP=data.pivot("month","year","births")
print(dataP)

sns.heatmap(dataP, annot=True, fmt="d")
plt.show()