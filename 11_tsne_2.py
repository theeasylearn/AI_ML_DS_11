# ---------------------------------------------------------

# ---------------------------------------------------------
# Import required libraries
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
from sklearn.datasets import fetch_openml
# ---------------------------------------------------------
# STEP 1: Load the dataset
# ---------------------------------------------------------
fashion = fetch_openml(name="Fashion-MNIST",version=1,as_frame=False)

X = fashion.data
y = fashion.target

print(X.shape)
print(y.shape)

#scaling 
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#CREATE MODEL
model = TSNE(n_components=2,perplexity=30,random_state=42)
t_sne = model.fit_transform(X_scaled)

#create plot 
plt.figure(figsize=(10,7))
scatter = plt.scatter(t_sne[:,0],t_sne[:,1],c=y,s=25,cmap="tab10")
plt.xlabel("First component")
plt.ylabel("Second component")
plt.title("T-SNE algorithm")
plt.colorbar(scatter,label = "cloths")
plt.show()
