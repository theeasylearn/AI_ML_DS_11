import matplotlib.pyplot as plt 
import math
import numpy as np 

degrees = [190, 90, 135, 45, 15, 315, 270, 225, 160, 110, 180]
radians = [round(deg * math.pi / 180, 6) for deg in degrees]

cricket_positions = [
    "First Slip",
    "Point",
    "Cover",
    "Mid-off",
    "Long-on",
    "Mid-wicket",
    "Square Leg",
    "Fine Leg",
    "Third Man",
    "Gully",
    "Wicket-keeper"
]

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.set_theta_zero_location('N')  # Sets 0° to the Top (North)
ax.set_theta_direction(-1)       # Clockwise

# Arbitrary radial distances (radii) set to 1 for layout structure
radii = list(np.ones(len(degrees)))

# Plot the positions
ax.scatter(radians, radii, color='red', zorder=3)

# --- Add field positions as labels ---
for theta, r, label in zip(radians, radii, cricket_positions):
    ax.annotate(
        label, 
        xy=(theta, r),             # Target coordinates
        xytext=(0, 8),             # Shift text 8 points vertically away from dot
        textcoords="offset points",# Coordinate system for xytext
        ha='center',               # Horizontal alignment
        va='bottom',               # Vertical alignment
        fontsize=9,
    )

# Clean up layout by removing the radial grid lines/labels since radii are arbitrary
ax.set_yticklabels([])

plt.tight_layout()
plt.show()