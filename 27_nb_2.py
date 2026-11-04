import kagglehub
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, PowerTransformer
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, accuracy_score

# 1. Load dataset
path = kagglehub.dataset_download("sergionefedov/will-this-order-come-back")
print(f"Dataset path: {path}")
df = pd.read_csv(f"{path}/fashion_returns_master.csv")
print(f"Initial shape: {df.shape}")

# =====================================================================
# 2. FEATURE SELECTION & TARGET MAPPING
# =====================================================================
# FIX 1: Use integer keys (0, 1) instead of strings ("0", "1")
status_mapping = {
    0: "not returned",
    1: "returned"
}
df["returned"] = df["returned"].map(status_mapping)

# FIX 2: Removed duplicate "avg_review_rating"
continuous_cols = [
    "price_usd",        
    "discount_pct",   
    "customer_prior_orders",  
    "customer_prior_return_rate",          
    "avg_review_rating",          
    "num_reviews",          
    "days_to_delivery"        
]

binary_cols = [
    'is_premium', 'ordered_multiple_sizes', 'reviews_read', 
    'size_chart_viewed', 'model_shown', 'is_gift', 'return_shipping_free'
]

nominal_cols = ['marketplace_region', 'category', 'fabric', 'fit_type', 'device']

ordinal_cols = ['size_ordered', 'size_usual', 'size_mismatch']

# FIX 3: Drop 'return_reason' (which is NaN for non-returns) BEFORE calling dropna()
df = df.drop(columns=['order_id', 'return_reason'])
df = df.dropna()
print(f"Shape after cleaning: {df.shape}")

X = df.drop(columns=['returned'])
y = df['returned']

# =====================================================================
# 3. PREPROCESSING & PIPELINE
# =====================================================================
preprocessor = ColumnTransformer(
    transformers=[
        ('numerical_transformer', PowerTransformer(method='yeo-johnson'), continuous_cols),
        ('ordinal_transformer', OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1), ordinal_cols),
        ('binary_transformer', OneHotEncoder(drop='if_binary', sparse_output=False), binary_cols),
        ('nominal_transformer', OneHotEncoder(
            drop='first', 
            handle_unknown='ignore', 
            sparse_output=False
        ), nominal_cols)
    ]
)

model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', GaussianNB(var_smoothing=1e-2))
])

# =====================================================================
# 4. TRAIN / TEST SPLIT & EVALUATION
# =====================================================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)

print("\n=== Model Performance ===")
# FIX 4: Fixed multiplication syntax in f-string
print(f"Test Accuracy: {acc * 100:.2f}%\n")
print("Classification Report:")
print(classification_report(y_test, y_pred))