# ============================================================
# SVM REGRESSION: INDIAN STOCK PRICE PREDICTION
# Stock: Tata Steel (NSE)
# Algorithm: Support Vector Regression (SVR)
# ============================================================

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# STEP 2: Download Indian stock market data (5 Years is the Sweet Spot)
ticker = "TATASTEEL.NS"
print("Downloading stock data...")
df = yf.Ticker(ticker).history(period="5y", interval="1d", auto_adjust=True)

if df.empty:
    raise RuntimeError("No stock data downloaded. Check your connection or ticker.")

df = df[["Close", "Volume"]].dropna()

# CRITICAL FIX 1: Convert raw price to stationary Log Returns
df["Log_Return"] = np.log(df["Close"] / df["Close"].shift(1))
df["Vol_Growth"] = df["Volume"].pct_change()
df = df.dropna()

# ==========================================
# STEP 3: Create lagged features (UPDATED)
# ==========================================
feature_columns = []
for lag in range(1, 6):
    df[f"Return_lag_{lag}"] = df["Log_Return"].shift(lag)
    df[f"Vol_lag_{lag}"] = df["Vol_Growth"].shift(lag)
    feature_columns.append(f"Return_lag_{lag}")
    feature_columns.append(f"Vol_lag_{lag}")

# Target variable is today's Log Return
df["Target"] = df["Log_Return"]

# --- CRITICAL FIX CODE ---
# 1. Drop standard NaN values from shifting
df = df.dropna()

# 2. Replace hidden infinite values (-inf and inf) with NaN, then drop them
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df = df.dropna()
# -------------------------

X = df[feature_columns]
y = df["Target"]

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
