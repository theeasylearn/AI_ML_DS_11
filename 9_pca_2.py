# ============================================================
# PCA - PATIENT HEALTH ANALYSIS
# ============================================================

# Step 1: Import libraries

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
# Install dependencies as needed:
# pip install kagglehub[pandas-datasets]
import kagglehub
from kagglehub import KaggleDatasetAdapter
# Set the path to the file you'd like to load
file_path = "wine-clustering.csv"
# Load the latest version
df = kagglehub.load_dataset(KaggleDatasetAdapter.PANDAS,"harrywang/wine-dataset-for-clustering",file_path,)
# print("First 5 records:", df.head())
print("Size of dataset ",df.shape)

#scalling 
scaler = StandardScaler()
x_scaled = scaler.fit_transform(df)
print(x_scaled)
#create model
model = PCA(n_components=2)
data = model.fit_transform(x_scaled)

#create dataframe
pca_df = pd.DataFrame(data,columns=['PC1','PC2'])
print(pca_df)