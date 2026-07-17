import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
result = pd.read_csv('marks.csv')
sns.boxplot(data=result,x='Division',y='Mark')
plt.xlabel("Division")
plt.ylabel("Mark")
plt.grid(which='both')
plt.show()

