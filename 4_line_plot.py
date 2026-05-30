import matplotlib.pyplot as plt
import numpy as np
# Gujarat Titans cumulative over-by-over runs (IPL 2026 Qualifier 2 vs RR)
score = [11, 24, 38, 52, 63, 75, 87, 99, 108, 127, 142, 156, 168, 178, 182, 189, 200, 205, 219]
overs = np.arange(1,len(score)+1)
print(overs)
plt.figure(figsize=(10,6))
plt.plot(overs,score,marker='o',color='blue',label='GT')
plt.xlabel('Overs')
plt.xticks(overs)
plt.yticks(np.arange(0, max(score)+20, 10))
plt.ylabel('Runs')
plt.title('Gujarat Titans Runs(IPL 2026 Qualifier 2 vs RR)')
plt.legend(loc='upper left')
plt.grid(which='both', linestyle='--', linewidth=0.5)
plt.show()
