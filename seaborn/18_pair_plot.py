import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
result = sns.load_dataset('titanic')
sns.pairplot(result,hue='survived',diag_kind='kde')
plt.suptitle("Pair plot chart",y=1.02)
plt.show()