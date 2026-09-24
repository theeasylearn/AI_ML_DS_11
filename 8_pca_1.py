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
print(df)

# ============================================================
# Step 3: Select input features
# ============================================================

X = df[
    [
        "Age",
        "Systolic_BP",
        "Diastolic_BP",
        "Cholesterol",
        "Glucose",
        "BMI",
        "Heart_Rate",
        "Activity"
    ]
]
# ============================================================
# Step 4: Standardize the data
# ============================================================
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
# Display standardized data
print("\nStandardized Data:")



# ============================================================
# Step 5: Apply PCA
# ============================================================
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)


# ============================================================
# Step 6: Create PCA DataFrame
# ============================================================
pca_df = pd.DataFrame(
    X_pca,
    columns=["PC1", "PC2"]
)
# Add patient names

pca_df["Patient"] = df["Patient"]


# ============================================================
# Step 7: Display PCA results
# ============================================================

print("\nPCA Results:")
print(pca_df)


# ============================================================
# Step 8: Display explained variance
# ============================================================

print("\nExplained Variance Ratio:")

print("PC1 : ",pca.explained_variance_ratio_[0])

print("PC2:",pca.explained_variance_ratio_[1])


# Total information retained

total_variance = (
    pca.explained_variance_ratio_[0]
    +
    pca.explained_variance_ratio_[1]
)

print("\nTotal Variance Retained:",
      total_variance)


# ============================================================
# Step 9: Display PCA components
# ============================================================

components = pd.DataFrame(
    pca.components_,
    columns=X.columns,
    index=["PC1", "PC2"]
)

print("\nPCA Components:")
print(components)
# exit(0)

# ============================================================
# Step 10: Visualize PCA results
# ============================================================

plt.figure(figsize=(10, 6))

plt.scatter(
    pca_df["PC1"],
    pca_df["PC2"],
    s=100)


# Add patient names
for i in range(len(pca_df)): # 0 to 11

    plt.annotate(
        pca_df.loc[i, "Patient"],
        (
            pca_df.loc[i, "PC1"],
            pca_df.loc[i, "PC2"]
        ),
        xytext=(5, 5),
        textcoords="offset points"
    )
plt.xlabel("Principal Component 1 (PC1)")
plt.ylabel("Principal Component 2 (PC2)")
plt.title("PCA - Patient Health Analysis")
plt.axhline(0)
plt.axvline(0)
plt.show()