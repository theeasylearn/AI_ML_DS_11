import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
result = pd.read_csv('marks.csv')
# print(result)
sns.pointplot(data=result,x='Division',y='Mark',)
plt.grid(which='both')
plt.title("Strip plot chart of Students marks (division wise)")
plt.xlabel('Division')
plt.ylabel('Mark')
plt.show()