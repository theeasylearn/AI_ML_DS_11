import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
result = pd.read_csv('marks.csv')

# print(score)
sns.histplot(x='Mark',data=result,kde=False,color='yellow',bins=10)
plt.xlabel('marks')
plt.ylabel('score')
plt.show()

