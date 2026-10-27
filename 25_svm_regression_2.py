# ============================================================
# SVM REGRESSION: Healthcare Actuarial & Insurance Pricing
# The Problem: Estimating individual medical insurance charges from age, sex, BMI, children, smoking status, and region.
# Algorithm: Support Vector Regression (SVR)
# ============================================================
import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.compose import ColumnTransformer, TransformedTargetRegressor
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
import kagglehub

from sklearn.svm import SVR
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, root_mean_squared_error

path = kagglehub.dataset_download("shubham001official/indian-health-insurance-claims-analysis")

print("Path to dataset files:", path)
df = pd.read_csv(path + "/indian_health_insurance_claims_dataset.csv")

# df = df[["Close", "Volume"]].dropna()
# print('before drop ', df.shape)


print(df.shape)
# annual_income_inr, sum_insured, total_claim_amount, gender, policy_start_date, claim_date

def parse_inr_and_lpa(val):
    """Converts '₹1,45,000', '8.5 LPA', or numeric strings into clean float INR."""
    if pd.isna(val):
        return np.nan
    s = str(val).upper().strip()
    is_lpa = "LPA" in s or "LAKH" in s
    # Extract numeric part (including decimals)
    cleaned = re.sub(r"[^0-9.]","", s)
    if cleaned == "" or cleaned == ".":
        return np.nan
    num = float(cleaned)
    return num * 100000.0 if is_lpa else num

# Clean currency columns
for col in ["annual_income_inr", "sum_insured", "total_claim_amount"]:
    if col in df.columns:
        df[col] = df[col].apply(parse_inr_and_lpa)
    
# Drop rows where the target itself is missing or non-positive
df = df.dropna(subset=["total_claim_amount"])
df = df[df["total_claim_amount"] > 0].copy()

if "policy_start_date" in df.columns and "claim_date" in df.columns:
    start_dt = pd.to_datetime(df["policy_start_date"], errors="coerce")
    claim_dt = pd.to_datetime(df["claim_date"], errors="coerce")
    df["policy_age_days"] = (claim_dt - start_dt).dt.days.clip(lower=0)

# Fix inconsistent gender values ('M', 'male', 'Male', 'F', 'female')
if "gender" in df.columns:
    df["gender"] = (
        df["gender"].astype(str).str.strip().str.upper()
        .map({"M": 1, "MALE": 1, "F": 0, "FEMALE": 0})
    )

df = df.drop(columns=["hospital_bill_amount", "pre_hospitalization_expense",
    "post_hospitalization_expense", "non_payable_items",
    "deductible_amount", "co_pay_amount",
    "policy_id", "customer_name", "aadhaar_masked",
    "pincode", "hospital_name", "city",
    "policy_start_date", "claim_date"])

X = df 
y = df["total_claim_amount"]

print(X)
num_cols = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
cat_cols = X.select_dtypes(include=["object", "category", "bool"]).columns.tolist()

print("Numerical Columns ",num_cols)
print("Categorical columns ", cat_cols)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#Just create pipline (but not used)
numeric_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(drop="first", handle_unknown="ignore"))
])


preprocessor = ColumnTransformer([
    ("num", numeric_transformer, num_cols),
    ("cat", categorical_transformer, cat_cols)
])


#Actually use pipeline
# SVR with Log-Target Transformation (handles heavy right-skew in INR claims)
svr_pipeline = Pipeline([
    ("prep", preprocessor),
    ("svr", SVR(kernel="rbf", C=10.0, epsilon=0.05, gamma="scale", cache_size=1500))
])

svr_log_model = TransformedTargetRegressor(
    regressor=svr_pipeline,
    func=np.log1p,
    inverse_func=np.expm1
)

svr_log_model.fit(X_train, y_train)
pred_svr = svr_log_model.predict(X_test)

# Evaluate SVR directly
print(f"SVR R2 Score : {r2_score(y_test, pred_svr):.4f}")
print(f"SVR RMSE     : ₹{root_mean_squared_error(y_test, pred_svr):,.2f}")
print(f"SVR MAE      : ₹{mean_absolute_error(y_test, pred_svr):,.2f}")

print("Columns inside X_train:", list(X_train.columns))
train_pred = svr_log_model.predict(X_train)
print(f"Train R2 : {r2_score(y_train, train_pred):.4f}")
print(f"Test  R2 : {r2_score(y_test, pred_svr):.4f}")
