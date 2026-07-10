import matplotlib.pyplot as plt 
temperature_1 = [0.61, 0.0, 3.89, 5.61, 8.28, 2.22, 2.78, -2.78, -2.78, 2.22, -0.61, 2.78]
temperature_2 = [1.61, 0.8, -2.5, 2.61, 0.28, -2.22, -2.78, 2.78, -3.78, -2.22, 1.61, 3.78]

days = list(range(1,len(temperature_1)+1))

plt.stackplot(days,temperature_1,temperature_2)
plt.xlabel('days')
plt.xticks(ticks=days)
plt.ylabel('temperature')
plt.show()