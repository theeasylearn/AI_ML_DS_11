# ---------------------------------------------------------
# T-SNE EXAMPLE
# Handwritten Digit Visualization
# ---------------------------------------------------------
# Import required libraries
import matplotlib.pyplot as plt

from sklearn.datasets import load_digits
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
# ---------------------------------------------------------
# STEP 1: Load the dataset
# ---------------------------------------------------------
digits = load_digits()

#create x and y 
X = digits.data 

Y = digits.target 
# print(X.shape)

#scaling 
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#create mode
model = TSNE(n_components=2,perplexity=30,random_state=42)

t_sne = model.fit_transform(X_scaled)

#create plot 
plt.figure(figsize=(10,7))
scatter = plt.scatter(t_sne[:,0],t_sne[:,1],c=Y,s=25,cmap="tab10")
plt.xlabel("First component")
plt.ylabel("Second component")
plt.title("T-SNE algorithm")
plt.colorbar(scatter,label = "digits")
plt.show()
