import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1. Load the CSV file
df = pd.read_csv("tempreture.csv")

# 2. Extract the city names to use as y-axis labels later
cities = df["City"].values

# 3. Drop the 'City' column so only numerical temperature data remains
# Also extract the numerical values as a clean NumPy array
temperature_matrix = df.drop(columns=["City"]).values

# 4. Create the heatmap plot
plt.figure(figsize=(12, 6))
plt.imshow(temperature_matrix, cmap="hot", aspect="auto")

# 5. Add proper labels for clarity
plt.colorbar(label="Temperature (°C)")  # Adds the color scale bar

# Set X-axis ticks for days 1 to 31
plt.xlabel("Day of Month")
plt.xticks(
    ticks=np.arange(31), labels=np.arange(1, 32)
)  # Maps 0-30 index to days 1-31

# Set Y-axis ticks to show actual City names
plt.ylabel("City")
plt.yticks(ticks=np.arange(len(cities)), labels=cities)

plt.title("Gujarat Cities Temperature Heatmap - May 2026")
plt.tight_layout()
plt.show()