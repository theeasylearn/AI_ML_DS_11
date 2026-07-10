import matplotlib.pyplot as plt 
temperature = [0.61, 0.0, 3.89, 5.61, 8.28, 2.22, 2.78, -2.78, -2.78, 2.22, -0.61, 2.78, 10.61, 8.28, 6.72, 6.72, 2.78, -0.61, -1.11, -1.11, -0.61, 10.0, 5.0, 6.11, 8.28, 7.78, 1.11, 2.78, 2.22, 7.78]

max_temperature = [20.0, 20.0, 10.0, 23.28, 23.89, 10.61, 6.72, 13.28, 13.89, 11.11, 13.28, 22.78, 25.0, 26.72, 23.89, 18.28, 11.11, 2.22, 4.39, 1.72, 13.89, 19.39, 22.22, 25.0, 25.0, 15.0, 16.72, 16.72, 17.78, 19.39]

days = list(range(1,len(temperature)+1))

plt.fill_between(days,temperature,color='cyan',alpha=0.5)
plt.fill_between(days,max_temperature,color='orange',alpha=0.5)
plt.xlabel('days')
plt.xticks(ticks=days)
plt.ylabel('temperature')
plt.show()