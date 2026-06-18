import matplotlib.pyplot as plt 
import numpy as np 

plt.subplot(1,2,1)
score = [11, 24, 38, 52, 63, 75, 87, 99, 108, 127, 142, 156, 168, 178, 182, 189, 200, 205, 219]
overs = np.arange(1,len(score)+1)
print(overs)
plt.plot(overs,score,marker='o',color='blue',label='GT')
plt.xlabel('Overs')
plt.xticks(overs)
plt.yticks(np.arange(0, max(score)+20, 10))
plt.ylabel('Runs')
plt.title('Gujarat Titans Runs(IPL 2026 Qualifier 2 vs RR)')
plt.legend(loc='upper left')
plt.grid(which='both', linestyle='--', linewidth=0.5)

plt.subplot(1,2,2)
runs_per_over = [11, 13, 14, 14, 11, 12, 12, 12, 9, 19, 15, 14, 12, 10, 4, 7, 11, 5, 14]
overs = list(range(1,20))
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


plt.tight_layout()
plt.show()
