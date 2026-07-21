import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
result = pd.read_csv('marks.csv')
print(result)
sns.stripplot(data=result,x='Division',y='Mark',jitter=True)
plt.title("Strip plot chart of Students marks (division wise)")
plt.show()