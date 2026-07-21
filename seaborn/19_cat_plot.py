import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
result = pd.read_csv('marks.csv')
sns.catplot(data=result,x='Division',y="Mark",kind='box')
plt.xlabel("Division")
plt.ylabel('Marks')
plt.show()