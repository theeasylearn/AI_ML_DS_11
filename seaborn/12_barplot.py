import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
maruti = pd.read_csv('maruti.csv')

sns.barplot(data=maruti,x='year',y='units',hue='type')
plt.xlabel('year')
plt.ylabel('units')
plt.tight_layout()
plt.show()