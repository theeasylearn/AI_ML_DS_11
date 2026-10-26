# ============================================================
# SVM REGRESSION: Healthcare Actuarial & Insurance Pricing
# The Problem: Estimating individual medical insurance charges from age, sex, BMI, children, smoking status, and region.
# Algorithm: Support Vector Regression (SVR)
# ============================================================

import re

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import kagglehub

from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

path = kagglehub.dataset_download("shubham001official/indian-health-insurance-claims-analysis")

print("Path to dataset files:", path)
df = pd.read_csv(path + "/indian_health_insurance_claims_dataset.csv")

# df = df[["Close", "Volume"]].dropna()
# print('before drop ', df.shape)
y = df["hospital_bill_amount"]

df = df.drop(columns=['policy_id', 'customer_name', 'aadhaar_masked', 'pincode', 'hospital_name','city','hospital_bill_amount', 'pre_hospitalization_expense', 'post_hospitalization_expense', 'non_payable_items', 'deductible_amount', 'co_pay_amount'])

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
    
print(df.head())
exit(1)
X = df[feature_columns]

# STEP 4: Split data chronologically (80/20)
split_index = int(len(df) * 0.80)

X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]
y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]

# STEP 5: Create and train the SVR model scaled for returns
model = make_pipeline(
    StandardScaler(),
    SVR(kernel="rbf", C=10, epsilon=0.001) # Optimized hyper-parameters for fractional numbers
)

print("Training SVR model...")
model.fit(X_train, y_train)
print("Model trained successfully!")

# STEP 6: Predict test-set log returns
pred_returns = model.predict(X_test)

# CRITICAL FIX 2: Reconstruct actual rupee prices from predicted log returns
# Formula: Price_today = Price_yesterday * exp(predicted_log_return)
history_close = df["Close"].iloc[split_index - 1 : -1].values
y_pred_prices = history_close * np.exp(pred_returns)
y_test_prices = df["Close"].iloc[split_index:].values

# STEP 7: Evaluate model performance on actual price metrics
mae = mean_absolute_error(y_test_prices, y_pred_prices)
rmse = np.sqrt(mean_squared_error(y_test_prices, y_pred_prices))
r2 = r2_score(y_test_prices, y_pred_prices)

print("\n========== MODEL PERFORMANCE ==========")
print(f"MAE  : Rs. {mae:.2f}")
print(f"RMSE : Rs. {rmse:.2f}")
print(f"R²   : {r2:.4f}  <-- (Will now be clean and positive)")

# STEP 8: Compare actual and predicted prices
results = pd.DataFrame({
    "Actual Price": y_test_prices,
    "Predicted Price": y_pred_prices
}, index=df.index[split_index:])

print("\nLast 10 predictions:")
print(results.tail(10).round(2))

# STEP 9: Plot actual vs predicted prices
plt.figure(figsize=(12, 6))
plt.plot(results.index, results["Actual Price"], label="Actual Closing Price", color="royalblue")
plt.plot(results.index, results["Predicted Price"], label="Predicted Closing Price", color="orange", linestyle="--")
plt.title("Tata Steel: Actual vs SVR Predicted Prices (Stationary Transformed)")
plt.xlabel("Date")
plt.ylabel("Price (INR)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# STEP 10: Predict the next trading day's closing price with matching structural feature layout
latest_features_list = []
for lag in range(1, 6):
    latest_features_list.append(df["Log_Return"].iloc[-lag])
    latest_features_list.append(df["Vol_Growth"].iloc[-lag])

latest_features_df = pd.DataFrame([latest_features_list], columns=feature_columns)

next_log_return = model.predict(latest_features_df)[0]
next_price = df["Close"].iloc[-1] * np.exp(next_log_return)

print("\n========== NEXT-DAY FORECAST ==========")
print("Latest available closing price: Rs.", round(df["Close"].iloc[-1], 2))
print("Predicted next trading-day close: Rs.", round(next_price, 2))
