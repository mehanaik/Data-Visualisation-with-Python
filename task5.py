import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r'./tempYearly.csv')
print(data)

sns.jointplot("Rainfall","Temperature",data=data,kind="hex")
plt.show()

sns.jointplot("Rainfall","Temperature",data=data,kind="reg")
plt.show()