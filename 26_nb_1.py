import os
import kagglehub
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# =====================================================================
# 1. DOWNLOAD & LOAD KAGGLE DATASET
# =====================================================================
# Kaggle: aljarah/xapi-edu-data (Students' Academic Performance Dataset)
path = kagglehub.dataset_download("aljarah/xapi-edu-data")
print({path})

df = pd.read_csv(path + "/xAPI-Edu-Data.csv")
print(df.shape)

# exit(1)

# =====================================================================
# 2. FEATURE SELECTION & TARGET MAPPING
# =====================================================================
# Map academic class tiers to early-alert status:
# 'L' (Low-Level: 0-69)   -> 'At Risk'
# 'M' (Middle-Level: 70-89) -> 'Moderate'
# 'H' (High-Level: 90-100) -> 'On Track'
status_mapping = {
    "L": "At Risk",
    "M": "Moderate",
    "H": "On Track"
}
df["Risk_Alert"] = df["Class"].map(status_mapping)

# Continuous behavioral and LMS engagement metrics
continuous_features = [
    "raisedhands",        # Classroom questions / hand raises (0-100)
    "VisITedResources",   # LMS course content visits (0-100)
    "AnnouncementsView",  # Course announcement checks (0-100)
    "Discussion"          # Discussion forum participation (0-100)
]
target_col = "Risk_Alert"

X = df[continuous_features]
y = df[target_col]

# Split 75% training, 25% testing with stratification to preserve class balance
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# =====================================================================
# 3. TRAIN GAUSSIAN NAIVE BAYES
# =====================================================================
gnb = GaussianNB()
gnb.fit(X_train, y_train)

# =====================================================================
# 4. EVALUATION & METRICS
# =====================================================================
y_pred = gnb.predict(X_test)
acc = accuracy_score(y_test, y_pred)

print("=== Model Performance ===")
print(f"Test Accuracy: {acc * 100:.2f}%\n")

print("Classification Report:")
print(classification_report(y_test, y_pred))
