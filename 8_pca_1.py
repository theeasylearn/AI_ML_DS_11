# ============================================================
# PCA - PATIENT HEALTH ANALYSIS
# ============================================================

# Step 1: Import libraries

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
# ============================================================
# Step 2: Load dataset
# ============================================================
# Convert dictionary into DataFrame
df = pd.read_csv("patient_health_analysis.csv")
# Display original data
print("Original Dataset:")
#select input features 
Patient = df['Patient']
print(Patient)
del df['Patient']
# print(df)
#scaling 
scaler = StandardScaler()
x_scaled = scaler.fit_transform(df)
print(x_scaled)
#create model 
pca = PCA(n_components=2)
data = pca.fit_transform(x_scaled)
#create dataframe 
pca_df = pd.DataFrame(data,columns=['PC1','PC2'])
print(pca_df)
print('PC1 variance',pca.explained_variance_ratio_[0])
print('PC2 variance',pca.explained_variance_ratio_[1])

loadings = pd.DataFrame(
    pca.components_.T,
    columns=['PC1', 'PC2'],
    index=df.columns
)
print("Feature Loadings (Weights):")
print(loadings)

#create chart
plt.figure(figsize=(10,10))
plt.scatter(pca_df['PC1'],pca_df['PC2'],s=100)

pca_df ["Paitent"] = Patient
for i in range(len(pca_df)):
    plt.annotate(pca_df.loc[i,'Paitent'],(pca_df.loc[i,'PC1'],pca_df.loc[i,'PC2']),xytext=(5,5),textcoords="offset points")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.grid()
plt.show()
