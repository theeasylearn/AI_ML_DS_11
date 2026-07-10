import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
covid = pd.read_csv('covid_death.csv')

# Convert category to numeric
unique_cats = covid["category"].unique()
cat_mapping = {cat: i for i, cat in enumerate(unique_cats)}
covid["category_numeric"] = covid["category"].map(cat_mapping)

# Plot
plt.figure(figsize=(10, 6))
plt.hexbin(
    x=covid['age'], 
    y=covid['category_numeric'],
    gridsize=5, 
    cmap='viridis'
)

# Add colorbar
plt.colorbar(label='Count')

# Better y-axis labels
plt.yticks(ticks=range(len(unique_cats)), labels=unique_cats)

plt.xlabel('Age')
plt.ylabel('Category')
plt.title('Hexbin Plot: Age vs Category')
plt.grid(True, alpha=0.3)
plt.show()