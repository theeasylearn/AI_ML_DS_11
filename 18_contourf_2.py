import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
# Define the reference elevations (meters above sea level)
elevations = [0, 2860, 5364, 6400, 7900, 8848]
labels = [
    'Sea Level (0m)', 
    'Lukla (2,860m)', 
    'Base Camp (5,364m)', 
    'Camp II (6,400m)', 
    'Camp IV (7,900m)', 
    'Summit (8,848m)'
]

# Monthly average temperatures (°C) at these key elevations based on meteorological data
# Months mapped from January (index 0) to December (index 11)
temp_data = {
    0:    [18, 21, 26, 30, 32, 30, 29, 29, 28, 26, 22, 19],     # Sea Level reference for region
    2860: [3,  5,  9,  12, 14, 16, 17, 17, 15, 11, 7,  4],      # Lukla
    5364: [-17, -14, -10, -5, 0,  4,  6,  6,  3,  -5, -10, -15], # Everest Base Camp
    6400: [-25, -22, -17, -12, -8, -4, -2, -2, -5, -12, -18, -22], # Camp II
    7900: [-32, -31, -26, -22, -18, -14, -12, -12, -15, -22, -27, -30], # Camp IV
    8848: [-36, -35, -32, -26, -22, -20, -19, -19, -21, -27, -32, -35]  # Summit
}

months = np.arange(1, 13)
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Create a fine grid (200 elevation intervals) for high-precision contour plotting
fine_elevations = np.linspace(0, 8848, 200)
grid_temps = np.zeros((len(fine_elevations), len(months)))

# Linearly interpolate between the known data points for a smooth gradient
for m_idx, month in enumerate(months):
    temps_at_elev = [temp_data[el][m_idx] for el in elevations]
    f = interp1d(elevations, temps_at_elev, kind='linear')
    grid_temps[:, m_idx] = f(fine_elevations)

# Create a structured DataFrame and export to a CSV file
df_grid = pd.DataFrame(grid_temps, index=fine_elevations, columns=month_names)
df_grid.index.name = 'Elevation_m'
df_grid.to_csv('everest.csv')

# Plotting the contour chart using matplotlib subplots
fig, ax = plt.subplots(figsize=(10, 7))
X, Y = np.meshgrid(months, fine_elevations)

# Generate a filled contour map with 25 levels using a reversed Red-Yellow-Blue palette
contour = ax.contourf(X, Y, grid_temps, levels=25, cmap='RdYlBu_r')



# Format the color bar
cbar = fig.colorbar(contour, ax=ax)
cbar.set_label('Average Temperature (°C)', fontsize=12)

# Axis configuration
ax.set_xticks(months)
ax.set_xticklabels(month_names)
ax.set_xlabel('Month of the Year', fontsize=12, labelpad=10)
ax.set_ylabel('Elevation Above Sea Level (meters)', fontsize=12, labelpad=10)
ax.set_title('Mount Everest Temperature Profile by Elevation & Month', fontsize=14, pad=15, fontweight='bold')


ax.set_xlim(0.8, 14.5)  # Offset limit to prevent right-hand text labels from being clipped
plt.tight_layout()

# Save output figure to environment
# plt.savefig('everest_temperature_contour.png', dpi=300)
plt.show()