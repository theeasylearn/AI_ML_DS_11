import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
match = pd.read_csv('virat_kohli.csv')
plt.figure(figsize=(18,6))


# 1. Use plt.bar instead of rugplot. 
# We give it a height of 1 for each century, and a controlled width so they don't overlap.
sns.kdeplot(data=match,x='match',alpha=0.5,fill=True)
sns.rugplot(data=match, x='match', height=0.25, color='blue')
plt.title("Virat Kohli Century")
plt.xlabel('Match No')
plt.xticks(ticks=range(10,320,5), rotation=90)
plt.ylabel('Century')

# 3. Clean up margins so vertical text labels don't get cut off
plt.tight_layout()

plt.show()