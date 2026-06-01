import matplotlib.pyplot as plt 
import pandas as pd 

#load data 
covid = pd.read_csv('covid_death.csv').squeeze()

age = covid['age']

plt.hist(x=age,bins=10,density=True,color='red',alpha=0.5,label='age')

plt.xlabel('Age')
plt.ylabel('Probability')
plt.title('Covid 19 death')
plt.show()
