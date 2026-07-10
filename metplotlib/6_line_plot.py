import matplotlib.pyplot as plt
import numpy as np
# Gujarat Titans cumulative over-by-over runs (IPL 2026 Qualifier 2 vs RR)
score = [11, 24, 38, 52, 63, 75, 87, 99, 108, 127, 142, 156, 168, 178, 182, 189, 200, 205, 219,220]
score = np.array(score)
# Rajasthan Royals cumulative over-by-over runs (IPL 2026 Qualifier 2 vs GT)
score_2 = [11, 23, 35, 47, 59, 73, 85, 96, 111, 122, 131, 140, 149, 159, 168, 175, 184, 195, 203, 214]
score_2 = np.array(score_2)
print(len(score), len(score_2))

overs = np.arange(1,21)
print(overs)
plt.figure(figsize=(10,6))
plt.plot(overs,score,marker='o',color='blue',label='GT',markersize=8,linewidth=2)
plt.plot(overs,score_2,marker='o',color='pink',label='RR',markersize=8,linewidth=2)
plt.xlabel('Overs')
plt.xticks(overs)
plt.yticks(np.arange(0, max(score)+20, 10))
plt.ylabel('Runs')
plt.title('Gujarat Titans Runs(IPL 2026 Qualifier 2 vs RR)')
plt.legend(loc='upper left')
plt.grid(which='both', linestyle='--', linewidth=0.5)
plt.savefig("linegraph.png",dpi=300)
plt.show()
