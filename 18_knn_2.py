# pip install imbalanced-learn

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)
import kagglehub
from imblearn.over_sampling import SMOTE

# ============================================================
# 1. Download & Data Preparation
# ============================================================
path = kagglehub.dataset_download("nikhil1e9/loan-default")

df = pd.read_csv(path + "/Loan_default.csv")
df = df.dropna()

y = df['Default']

# Binary Fields (Use Label Encoding / Binary Encoding)
df['HasMortgage'] = df['HasMortgage'].map({'Yes': 1, 'No': 0})
df['HasDependents'] = df['HasDependents'].map({'Yes': 1, 'No': 0})
df['HasCoSigner'] = df['HasCoSigner'].map({'Yes': 1, 'No': 0})

# Ordinal Field
df['Education'] = df['Education'].map({
    'High School': 0, 
    "Bachelor's": 1, 
    "Master's": 2, 
    'PhD': 3
})

# Nominal Fields (Use One-Hot Encoding)
nominal_column = ['EmploymentType', 'MaritalStatus', 'LoanPurpose']
df = pd.get_dummies(df, columns=nominal_column, drop_first=True, dtype=int)

X = df.drop(['LoanID', 'Default'], axis=1)

print("Dataset Shape:", X.shape)
print("Target Shape:", len(y))

# ============================================================
# 2. Train-Test Split
# ============================================================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# ============================================================
# 3. Feature Scaling
# ============================================================
scaler = StandardScaler()
# Fit ONLY on training data to prevent data leakage, then transform both
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ============================================================
# 4. SMOTE (Balancing the Classes)
# ============================================================
print("Applying SMOTE to balance the training data...")
smote = SMOTE(random_state=42)
# Resample ONLY the scaled training data. Test data remains untouched.
X_train_balanced, y_train_balanced = smote.fit_resample(X_train_scaled, y_train)
print(f"Balanced Training Data Shape: {X_train_balanced.shape}")

# ============================================================
# 5. Evaluate Optimal k
# ============================================================
# Changed step to 2 so it only tests odd numbers (11, 13, 15...) 
# Testing even numbers in KNN can cause tie-votes and takes unnecessary computation time.
# neighbors = range(11, 52, 2) 
# f1_scores = []

# print("Evaluating optimal n_neighbors...")
# for k in neighbors:
#     knn = KNeighborsClassifier(n_neighbors=k)
#     # FIT ON BALANCED DATA
#     knn.fit(X_train_balanced, y_train_balanced) 
#     # PREDICT ON UNBALANCED, SCALED TEST DATA
#     y_pred = knn.predict(X_test_scaled) 
    
#     score = f1_score(y_test, y_pred) 
#     f1_scores.append(score)
#     print(f"k={k} | F1-Score: {score:.4f}")

# # Plot the Elbow Curve
# plt.figure(figsize=(10, 6))
# plt.plot(neighbors, f1_scores, marker='o', linestyle='dashed', color='blue')
# plt.title('Optimal k Value via F1-Score (SMOTE Applied)')
# plt.xlabel('Number of Neighbors (k)')
# plt.ylabel('F1-Score')
# plt.grid(True)
# plt.show()
# exit(1)
# ============================================================
# 4. Create KNN Model
# ============================================================
knn = KNeighborsClassifier(n_neighbors=51)

# FIXED: Train on the balanced SMOTE data
knn.fit(X_train_balanced, y_train_balanced)

y_pred = knn.predict(X_test_scaled)

# ============================================================
# 8. Confusion Matrix
# ============================================================
cm = confusion_matrix(y_test, y_pred)
TN, FP, FN, TP = cm.ravel()

# ============================================================
# 9. Precision, 10. Recall, 11. F1 Score
# ============================================================
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# ============================================================
# 13. ROC and AUC
# ============================================================
# FIXED: Grab index 1 for the 'Default' probability
y_probability = knn.predict_proba(X_test_scaled)[:, 1]
auc = roc_auc_score(y_test, y_probability)

# ============================================================
# 14. Print Results
# ============================================================
print("\n========================================")
print("   LOAN DEFAULT PREDICTION")
print("========================================")
print(f"Precision   : {precision:.4f}")
print(f"Recall      : {recall:.4f}")
print(f"F1 Score    : {f1:.4f}")
print(f"AUC         : {auc:.4f}")
print("\nConfusion Matrix:")
print(cm)
print("\nConfusion Matrix Values:")
print("True Negative :", TN)
print("False Positive:", FP)
print("False Negative:", FN)
print("True Positive :", TP)