import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler

# ---------------------------------------------------------
# STEP 1: Load the dataset
# ---------------------------------------------------------
fashion = fetch_openml(name="Fashion-MNIST", version=1, as_frame=False)

X = fashion.data
y = fashion.target.astype(int)

print("Original shape:", X.shape, y.shape)

# OPTIONAL BUT RECOMMENDED: Subsample for fast computation
# Remove or adjust this slice if you need the full 70k points
subset_size = 5000
indices = np.random.RandomState(42).choice(len(X), subset_size, replace=False)
X_sub = X[indices]
y_sub = y[indices]

# ---------------------------------------------------------
# STEP 2: Scale and Fit t-SNE
# ---------------------------------------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_sub)

model = TSNE(n_components=2, perplexity=30, random_state=42, n_jobs=-1)
t_sne = model.fit_transform(X_scaled)

# ---------------------------------------------------------
# STEP 3: Plot
# ---------------------------------------------------------
class_names = [
    "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"
]

plt.figure(figsize=(10, 7))
scatter = plt.scatter(
    t_sne[:, 0], t_sne[:, 1],
    c=y_sub,
    s=6,
    alpha=0.7,
    cmap="tab10"  # Safe across all Matplotlib versions
)

plt.xlabel("First component")
plt.ylabel("Second component")
plt.title("t-SNE on Fashion-MNIST")

# Align colorbar ticks to discrete bins
cbar = plt.colorbar(scatter, ticks=range(10))
cbar.ax.set_yticklabels(class_names)

plt.tight_layout()
plt.show()