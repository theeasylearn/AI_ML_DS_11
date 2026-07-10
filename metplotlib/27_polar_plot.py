import matplotlib.pyplot as plt 
import math
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
ax.set_theta_direction(-1) #clock wise
plt.polar(degrees,radians)
plt.show()
