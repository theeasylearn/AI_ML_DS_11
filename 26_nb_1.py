import os

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, PowerTransformer
import kagglehub
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, accuracy_score

# =====================================================================
# 1. DOWNLOAD & LOAD KAGGLE DATASET
# =====================================================================
# Kaggle: aljarah/xapi-edu-data (Students' Academic Performance Dataset)
path = kagglehub.dataset_download("aljarah/xapi-edu-data")
print(path)

df = pd.read_csv(path + "/xAPI-Edu-Data.csv")
print(df.shape)
print(df.columns.to_list())
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

continuous_cols = [
    "raisedhands",        # Classroom questions / hand raises (0-100)
    "VisITedResources",   # LMS course content visits (0-100)
    "AnnouncementsView",  # Course announcement checks (0-100)
    "Discussion"          # Discussion forum participation (0-100)
]

binary_cols = [
    'gender', 'Semester', 'Relation', 
    'ParentAnsweringSurvey', 'ParentschoolSatisfaction', 'StudentAbsenceDays'
]

# Nominal columns (Note: you can test dropping 'PlaceofBirth' to reduce collinearity)
nominal_cols = ['SectionID', 'Topic', 'NationalITy', 'PlaceofBirth']

ordinal_cols = ['StageID', 'GradeID']
stage_order = ['lowerlevel', 'MiddleSchool', 'HighSchool']

grade_order = [
    'G-02', 'G-04', 'G-05', 'G-06', 'G-07', 
    'G-08', 'G-09', 'G-10', 'G-11', 'G-12'
]

target_map = {'L': 0, 'M': 1, 'H': 2}

X = df.drop(columns=['Class'])
y = df['Class'].map(target_map)

#preprocessing is process we perform on dataset before we use it to train model 
#to set order for all task in preprocessing we need to use ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ('numerical transformer', PowerTransformer(method='yeo-johnson'), continuous_cols),
        ('ordinal transformer', OrdinalEncoder(categories=[stage_order, grade_order]), ordinal_cols),
        ('binary transformer', OneHotEncoder(drop='if_binary', sparse_output=False), binary_cols),
        ('nominal transformer', OneHotEncoder(
            drop='first', 
            min_frequency=10,        # Groups rare countries into one bucket
            handle_unknown='ignore', 
            sparse_output=False
        ), nominal_cols)
    ]
)

# 5. Connect to GaussianNB (var_smoothing stabilizes dummy variable variances)
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', GaussianNB(var_smoothing=1e-2))
])

# Split 75% training, 25% testing with stratification to preserve class balance
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print("=== Model Performance ===")
print(f"Test Accuracy: {acc * 100:.2f}%\n")
print("Classification Report:")
print(classification_report(y_test, y_pred))