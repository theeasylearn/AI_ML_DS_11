import kagglehub
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# --------------------------------------------------
# 1. Download dataset from Kaggle
# --------------------------------------------------
print("Downloading dataset...")
path = kagglehub.dataset_download("youssefaboelwafa/hotel-booking-cancellation-prediction")

# --------------------------------------------------
# 2. Load dataset
# --------------------------------------------------
df = pd.read_csv(path + "/booking.csv")

# --------------------------------------------------
# 3. Clean column names
# --------------------------------------------------
df.columns = df.columns.str.strip()

# --------------------------------------------------
# 4. Convert categorical values into numbers
# --------------------------------------------------
# Binary Encoding for the target
df['booking status'] = df['booking status'].map({'Canceled': 1, 'Not_Canceled': 0})

# One-Hot Encoding for nominal categorical features
nominal_columns = ['type of meal', 'room type', 'market segment type']
df = pd.get_dummies(df, columns=nominal_columns, drop_first=True, dtype=int) 

# --------------------------------------------------
# 5 & 6. Select input features (X) and target (y)
# --------------------------------------------------
X = df.copy().drop(columns=['Booking_ID', 'date of reservation', 'booking status'])
y = df["booking status"]

# --------------------------------------------------
# 7. Split data
# --------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# --------------------------------------------------
# 8. Setup GridSearchCV for Hyperparameter Tuning
# --------------------------------------------------
print("\nStarting Grid Search for optimal hyperparameters...")
param_grid = {
    'max_depth': [5, 8, 10, 12, 15, 20],
    'min_samples_split': [2, 5, 10, 20, 50]
}

dt_base = DecisionTreeClassifier(criterion="gini", random_state=42)

grid_search = GridSearchCV(
    estimator=dt_base,
    param_grid=param_grid,
    scoring='accuracy', 
    cv=5,               
    n_jobs=-1,          
    verbose=1           
)

# --------------------------------------------------
# 9. Train Model (Executes Grid Search)
# --------------------------------------------------
grid_search.fit(X_train, y_train)

# Extract the best model found during the search
best_model = grid_search.best_estimator_

# --------------------------------------------------
# 10 & 11. Make predictions & Check metrics
# --------------------------------------------------
y_pred = best_model.predict(X_test)

print("\n" + "="*50)
print("Optimal Hyperparameters Found:")
print(grid_search.best_params_)
print("="*50)
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# --------------------------------------------------
# 12. Visualize Feature Importances
# --------------------------------------------------
importances = best_model.feature_importances_
feature_names = X.columns

# Create a DataFrame and sort by importance
importance_df = pd.DataFrame({
    'Feature': feature_names, 
    'Importance': importances
}).sort_values(by='Importance', ascending=False)

# Plot the Top 10 most important features
plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=importance_df.head(10), hue='Feature', legend=False, palette='mako')

plt.title('Top 10 Drivers of Hotel Booking Cancellations\n(Optimized Decision Tree)')
plt.xlabel('Gini Importance')
plt.ylabel('Feature')
plt.tight_layout()
plt.show()