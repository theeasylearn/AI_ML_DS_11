# ============================================================
# IMPROVED HOUSE PRICE PREDICTION PIPELINE
# ============================================================
import kagglehub
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# ------------------------------------------------------------
# STEP 1–4: Download and load dataset
# ------------------------------------------------------------
path = kagglehub.dataset_download("yasserh/housing-prices-dataset")
df = pd.read_csv(path + "/Housing.csv")

# ------------------------------------------------------------
# STEP 8 (UPGRADED): Encode ALL categorical features & engineer ratios
# ------------------------------------------------------------
# 1. Map all binary yes/no columns to 1/0
binary_cols = [
    "mainroad",
    "guestroom",
    "basement",
    "hotwaterheating",
    "airconditioning",
    "prefarea"
]

for col in binary_cols:
    df[col] = df[col].map({"yes": 1, "no": 0})

# 2. Encode furnishingstatus (ordinal: unfurnished=0, semi-furnished=1, furnished=2)
furnishing_map = {
    "unfurnished": 0,
    "semi-furnished": 1,
    "furnished": 2
}
df["furnishing_code"] = df["furnishingstatus"].map(furnishing_map)

# 3. Engineer domain interaction features for tree splits
df["area_per_bedroom"] = df["area"] / df["bedrooms"]
df["bath_to_bed_ratio"] = df["bathrooms"] / df["bedrooms"]
df["total_rooms"] = df["bedrooms"] + df["bathrooms"] + df["guestroom"] + df["basement"]

df["amenity_score"] = (
    df["mainroad"]
    + df["guestroom"]
    + df["basement"]
    + df["hotwaterheating"]
    + (df["airconditioning"] * 2)  # AC carries a higher market premium
    + (df["prefarea"] * 2)         # Preferred location carries a higher premium
    + df["furnishing_code"]
)

feature_cols = [
    "area", "bedrooms", "bathrooms", "stories", "parking",
    "mainroad", "guestroom", "basement", "hotwaterheating",
    "airconditioning", "prefarea", "furnishing_code",
    "area_per_bedroom", "bath_to_bed_ratio", "total_rooms", "amenity_score"
]

X = df[feature_cols]
y = df["price"]

# ------------------------------------------------------------
# STEP 10: Split dataset (same 80/20 split and random_state=42)
# ------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

# Log-transform target to reduce skew from luxury outliers
y_train_log = np.log1p(y_train)

# ------------------------------------------------------------
# STEP 11 & 12 (UPGRADED): Hyperparameter Tuning for Decision Tree
# ------------------------------------------------------------
param_grid = {
    "criterion": ["squared_error", "friedman_mse", "absolute_error"],
    "max_depth": [4, 5, 6, 7, 8, None],
    "min_samples_split": [5, 10, 15, 20],
    "min_samples_leaf": [3, 5, 8, 12],
    "ccp_alpha": [0.0, 0.0005, 0.001, 0.002]
}

grid_dt = GridSearchCV(
    DecisionTreeRegressor(random_state=42),
    param_grid=param_grid,
    cv=5,
    scoring="r2",
    n_jobs=-1
)

grid_dt.fit(X_train, y_train_log)
best_dt = grid_dt.best_estimator_

print("Best Decision Tree Parameters:")
print(grid_dt.best_params_)

# Convert log predictions back to rupees
y_pred_dt = np.expm1(best_dt.predict(X_test))

# ------------------------------------------------------------
# OPTIONAL UPGRADE: Random Forest & Gradient Boosting Ensembles
# ------------------------------------------------------------
rf_model = RandomForestRegressor(
    n_estimators=300,
    max_depth=10,
    min_samples_leaf=3,
    max_features=0.7,
    random_state=42,
    n_jobs=-1
)

rf_model.fit(X_train, y_train_log)
y_pred_rf = np.expm1(rf_model.predict(X_test))

gb_model = GradientBoostingRegressor(
    n_estimators=200,
    learning_rate=0.05,
    max_depth=3,
    min_samples_leaf=5,
    subsample=0.8,
    random_state=42
)
gb_model.fit(X_train, y_train_log)
y_pred_gb = np.expm1(gb_model.predict(X_test))

# ------------------------------------------------------------
# STEP 14–18: Compare Metrics Across Models
# ------------------------------------------------------------
def evaluate_model(name, y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_true, y_pred)
    print(f"\n--- {name} ---")
    print(f"MAE  : ₹{mae:,.2f}")
    print(f"RMSE : ₹{rmse:,.2f}")
    print(f"R²   : {r2:.4f}")

evaluate_model("Tuned Decision Tree (All Features)", y_test, y_pred_dt)
evaluate_model("Random Forest Regressor", y_test, y_pred_rf)
evaluate_model("Gradient Boosting Regressor", y_test, y_pred_gb)

# Show top feature importances from the tuned Decision Tree
importances = pd.Series(best_dt.feature_importances_, index=feature_cols).sort_values(ascending=False)
print("\nTop 8 Most Important Features (Decision Tree):")
print(importances.head(8).round(4))