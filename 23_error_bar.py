import numpy as np
import matplotlib.pyplot as plt

players = ['Virat Kohli', 'Rohit Sharma', 'Shubman Gill', 'Shreyas Iyer']
average = [58.72, 48.84, 55.00, 46.00]
errors = [4.1, 4.8, 5.2, 5.5]  #variance 

plt.errorbar(players,average,errors,color='blue',capsize=10,fmt='o')
plt.title("Player performance in ODI along with errors")
plt.xlabel("Players")
plt.ylabel("Runs")
plt.grid()
plt.tight_layout()
plt.show()