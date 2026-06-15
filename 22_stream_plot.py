import numpy as np
import matplotlib.pyplot as plt

# Create a grid
x = np.linspace(-5, 5, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

# Define velocity components (simulating a river flow)
U = np.ones_like(X) * 2       # Uniform flow in X direction
V = -np.sin(X) * np.cos(Y)    # Wavy flow in Y direction

# Plot
plt.figure(figsize=(10, 5))
plt.streamplot(X, Y, U, V, color='blue', linewidth=1, density=2)
plt.title("Basic River-like Stream Flow")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.tight_layout()
plt.show()