import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
result = pd.read_csv('marks.csv')
plt.figure(figsize=(12,6),dpi=200)
sns.violinplot(data=result,x='Division',y='Mark',hue='Gender')
plt.xlabel("Division")
plt.ylabel("Mark")
plt.yticks(ticks=(range(30,100,5)))
plt.grid(which='both')
plt.show()