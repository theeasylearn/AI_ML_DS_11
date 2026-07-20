import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
result = pd.read_csv('marks.csv')
# print(result)
sns.swarmplot(data=result,x='Division',y='Mark',size=4)
plt.grid(which='both')
plt.title("Strip plot chart of Students marks (division wise)")
plt.show()