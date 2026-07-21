import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
import numpy as np 
result = pd.read_csv('marks.csv')
# print(result)
sns.jointplot(data=result,x='Division',y='Mark',kind='scatter')
plt.grid(which='both')
plt.title("Join plot chart of Students marks (division wise)",y=1.2)
plt.xlabel('Division')
plt.ylabel('Mark')
plt.show()