import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
result = pd.read_csv('marks.csv')

# print(score)
sns.histplot(x='Mark',data=result,kde=True,color=['red','green','Blue','yellow'],bins=10,hue='Division')
plt.xlabel('marks')
plt.ylabel('score')
plt.show()

