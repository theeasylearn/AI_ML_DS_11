import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
journey = pd.read_csv('journey.csv')

sns.ecdfplot(x='Minutes',data=journey,color='green')
plt.title("ecdf chart")
plt.xlabel('Time')
plt.ylabel('KM')
plt.show()

