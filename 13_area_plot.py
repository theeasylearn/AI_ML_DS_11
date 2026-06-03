import matplotlib.pyplot as plt 
temperature = [0.61, 0.0, 3.89, 5.61, 8.28, 2.22, 2.78, -2.78, -2.78, 2.22, -0.61, 2.78, 10.61, 8.28, 6.72, 6.72, 2.78, -0.61, -1.11, -1.11, -0.61, 10.0, 5.0, 6.11, 8.28, 7.78, 1.11, 2.78, 2.22, 7.78]

days = list(range(1,len(temperature)+1))

plt.fill_between(days,temperature,color='cyan')
plt.xlabel('days')
plt.xticks(ticks=days)
plt.ylabel('temperature')
plt.show()