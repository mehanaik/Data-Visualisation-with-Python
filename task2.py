import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_json(r'./rain.json')

#graph for temperature
plt.figure(figsize=(15,5))
plt.plot( df['Month'],df['Temperature'],label='Temperature')
plt.show()

#graph for rainfall
plt.figure(figsize=(15,5))
plt.plot( df['Month'],df['Rainfall'],label='Rainfall')
plt.show()

#COMPARISION of both the graphs
plt.plot( df['Month'],df['Rainfall'],label='Rainfall')
plt.plot( df['Month'],df['Temperature'],label='Temperature')
plt.legend()
plt.show()