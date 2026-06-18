import matplotlib.pyplot as plt 
import pandas as pd 

#load csv 
result = pd.read_csv('marks.csv')
# print(result)
df = [
        result[result['Division'] == 'A']['Mark'],
        result[result['Division'] == 'B']['Mark'],
        result[result['Division'] == 'C']['Mark'],
        result[result['Division'] == 'D']['Mark'],
      ]
# print(df)
plt.violinplot(df,showmedians=True)
plt.ylabel("marks")
plt.xticks([1,2,3,4],['A','B','C','D'])
plt.show()
