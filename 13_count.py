import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
tips = sns.load_dataset('tips')
sns.countplot(data=tips,x='sex')
plt.xlabel("count of tips")
plt.ylabel("Gender")
plt.grid(which='both')
plt.show()

