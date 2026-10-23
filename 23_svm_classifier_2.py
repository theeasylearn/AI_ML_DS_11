
# SVM Classification: Email Spam Detection
# Dataset: Kaggle Spam Mails Dataset

# 1. Import libraries
from sklearn.preprocessing import StandardScaler

import kagglehub
import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    ConfusionMatrixDisplay
)
df = pd.read_csv("Phishing_Legitimate_full.csv")
print("\nFirst five rows:")
print(df.head())

print("\nDataset shape:", df.shape)
print("\nColumns:", df.columns.tolist())

feature_columns = ['NumDots', 'SubdomainLevel', 'PathLevel', 'UrlLength', 'NumDash', 'NumDashInHostname', 'AtSymbol', 'TildeSymbol', 'NumUnderscore', 'NumPercent', 'NumQueryComponents', 'NumAmpersand', 'NumHash', 'NumNumericChars', 'NoHttps', 'RandomString', 'IpAddress', 'DomainInSubdomains', 'DomainInPaths', 'HttpsInHostname', 'HostnameLength', 'PathLength', 'QueryLength', 'DoubleSlashInPath', 'NumSensitiveWords', 'EmbeddedBrandName', 'PctExtHyperlinks', 'PctExtResourceUrls', 'ExtFavicon', 'InsecureForms', 'RelativeFormAction', 'ExtFormAction', 'AbnormalFormAction', 'PctNullSelfRedirectHyperlinks', 'FrequentDomainNameMismatch', 'FakeLinkInStatusBar', 'RightClickDisabled', 'PopUpWindow', 'SubmitInfoToEmail', 'IframeOrFrame', 'MissingTitle', 'ImagesOnlyInForm', 'SubdomainLevelRT', 'UrlLengthRT', 'PctExtResourceUrlsRT', 'AbnormalExtFormActionR', 'ExtMetaScriptLinkRT', 'PctExtNullSelfRedirectHyperlinksRT']

X = df[feature_columns]
y = df["CLASS_LABEL"]
print(y.value_counts())
# exit(1)

# 5. Split training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)
print("\nTraining data:", len(X_train))
print("Testing data:", len(X_test))
# exit(1)


# 6. Create the SVM model
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("svm", LinearSVC(dual=False, max_iter=5000, random_state=42))
])

print("\nTraining SVM model...")
pipeline.fit(X_train, y_train)
print("Training completed!")

# 8. Evaluate the model
y_pred = pipeline.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("\nModel Accuracy:", round(accuracy * 100, 2), "%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

disp = ConfusionMatrixDisplay.from_estimator(
    pipeline,
    X_test,
    y_test,
    display_labels=["Legitimate (0)", "Phishing (1)"],
    cmap="Blues",
    values_format="d"
)
plt.title("LinearSVC Confusion Matrix (Phishing Detection)")
plt.tight_layout()
plt.show()

'''
Underwater Sonar Target Detection (Mines vs. Rocks)
Chronic Kidney Disease (CKD) Early Detection
'''