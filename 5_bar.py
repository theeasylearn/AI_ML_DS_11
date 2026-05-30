import matplotlib.pyplot as plt
import numpy as np
runs_per_over = [11, 13, 14, 14, 11, 12, 12, 12, 9, 19, 15, 14, 12, 10, 4, 7, 11, 5, 14]
overs = list(range(1,20))
plt.figure(figsize=(20,6))
bars = plt.bar(overs,runs_per_over, color='cyan', label='Runs per Over',edgecolor='black',width=0.9)
for bar in bars:
    bar.set_hatch('//')
    
plt.xticks(overs)
plt.yticks(np.arange(0, max(runs_per_over),2))
plt.xlabel('Overs')
plt.ylabel('Runs')
plt.title('Gujarat Titans Runs per over')
plt.legend(loc='upper left')
plt.grid(which='both', linestyle='--', linewidth=0.5)
plt.show()
