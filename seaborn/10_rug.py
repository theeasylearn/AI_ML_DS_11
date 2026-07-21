import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 

match = pd.read_csv('virat_kohli.csv')

plt.figure(figsize=(24,6))

# 1. Use plt.bar instead of rugplot. 
# We give it a height of 1 for each century, and a controlled width so they don't overlap.
sns.rugplot(data=match, x='match', height=0.50, color='blue')

plt.title("Virat Kohli Century")
plt.xlabel('Match No')
plt.xticks(ticks=range(10,320,5), rotation=90)
plt.ylabel('Century')

# 2. Limit the y-axis so the bars look neat and uniform
plt.ylim(0, 1.5)

# 3. Clean up margins so vertical text labels don't get cut off
plt.tight_layout()

plt.show()