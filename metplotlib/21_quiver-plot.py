import math
import matplotlib.pyplot as plt
import numpy as np

# 1. Raw Forecast Data for Bhavnagar, Gujarat
forecast_data = [
    {"time": "23:30 (Today)", "speed": 16, "direction": "southwest"},
    {"time": "00:30 (Tomorrow)", "speed": 14, "direction": "southwest"},
    {"time": "01:30", "speed": 14, "direction": "southwest"},
    {"time": "02:30", "speed": 13, "direction": "southwest"},
    {"time": "03:30", "speed": 12, "direction": "southwest"},
    {"time": "04:30", "speed": 12, "direction": "southwest"},
    {"time": "05:30", "speed": 11, "direction": "southwest"},
    {"time": "06:30", "speed": 13, "direction": "southwest"},
    {"time": "07:30", "speed": 13, "direction": "southwest"},
    {"time": "08:30", "speed": 12, "direction": "southwest"},
    {"time": "09:30", "speed": 12, "direction": "southwest"},
    {"time": "10:30", "speed": 11, "direction": "southwest"},
    {"time": "11:30", "speed": 11, "direction": "southwest"},
    {"time": "12:30", "speed": 13, "direction": "south"},
    {"time": "13:30", "speed": 14, "direction": "south"},
    {"time": "14:30", "speed": 17, "direction": "south"},
    {"time": "15:30", "speed": 19, "direction": "south"},
    {"time": "16:30", "speed": 20, "direction": "south"},
    {"time": "17:30", "speed": 20, "direction": "south"},
    {"time": "18:30", "speed": 19, "direction": "south"},
    {"time": "19:30", "speed": 19, "direction": "southwest"},
    {"time": "20:30", "speed": 18, "direction": "southwest"},
    {"time": "21:30", "speed": 17, "direction": "southwest"},
    {"time": "22:30", "speed": 17, "direction": "southwest"},
]

# Meteorological degrees (Direction the wind originates FROM)
direction_degrees = {
    "north": 0,
    "northeast": 45,
    "east": 90,
    "southeast": 135,
    "south": 180,
    "southwest": 225,
    "west": 270,
    "northwest": 315,
}

# 2. Extract components and convert angles to vector coordinates
times = [item["time"] for item in forecast_data]
speeds = [item["speed"] for item in forecast_data]

print(times,speeds)

#empty list
U = []
V = []

for item in forecast_data:
    deg = direction_degrees[item["direction"].lower()]
    rad = math.radians(deg)
    # Invert vectors so the arrows point TOWARD where the wind is going
    U.append(-item["speed"] * math.sin(rad))
    V.append(-item["speed"] * math.cos(rad))

# # Convert to arrays for mathematical plotting
X = np.arange(len(times))
Y = np.zeros(len(times))

# # 3. Plot Configuration
fig, ax = plt.subplots(figsize=(16, 6))

# # Use angles='uv' to break dependence on different X and Y axes limits
quiver = ax.quiver(
    X,
    Y,
    U,
    V,
    speeds,
    cmap="viridis",
    angles="uv",  # Uses the arrow components directly for the angle calculation
    pivot="middle",  # Anchors the center of the arrow on the coordinate point
    scale=180,  # Limits the length of the arrows so they stay clear of each other
)

# # 4. Interface Formatting
ax.set_xlim(-1, len(times))
ax.set_ylim(-15, 15)  # Creates space for the arrows to tilt upward/downward

ax.set_xticks(X)
ax.set_xticklabels(times, rotation=45, ha="right")
ax.set_yticks([])  # Hide Y-axis values for a clean horizontal timeline layout

ax.set_title(
    "Wind Velocity & Direction Timeline (Bhavnagar, Gujarat)",
    pad=20,
    fontsize=14,
    fontweight="bold",
)
ax.grid(axis="x", linestyle="--", alpha=0.5)

# # Horizontal colorbar positioned below the plot
cbar = fig.colorbar(
    quiver, ax=ax, orientation="horizontal", pad=0.25, shrink=0.7
)
cbar.set_label("Wind Speed (mph)", fontweight="bold")

plt.tight_layout()
plt.show()