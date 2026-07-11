import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 

#load dataset 
score = pd.read_csv('runs.csv')

# print(score.head(0))

#create chart
sns.scatterplot(x='sr_no',y='runs',data=score,hue='position',palette=['green','orange'])

plt.grid(which='both')
plt.legend(title='score',labels=['1','2'])
#show
plt.show()
