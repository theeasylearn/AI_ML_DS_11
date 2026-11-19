# Bernoulli Naive Bayes - tuned for higher precision on the Fake (1) class
# Same algorithm (BernoulliNB). The changes are to the features, the tuning and the decision threshold.
import os
import kagglehub
import numpy as np
import pandas as pd
from sklearn.model_selection import (
    train_test_split, GridSearchCV, StratifiedKFold, cross_val_predict, cross_val_score
)
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import (
    accuracy_score, balanced_accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, average_precision_score, confusion_matrix, classification_report,
    precision_recall_curve
)

# ==========================================
# 1. DOWNLOAD DATASET
# ==========================================
print("Downloading dataset via kagglehub...")
dataset_path = kagglehub.dataset_download("shivamb/real-or-fake-fake-jobposting-prediction")
df_raw = pd.read_csv(os.path.join(dataset_path, "fake_job_postings.csv"))
print(df_raw.shape)

# ==========================================
# 2. FEATURE ENGINEERING
# ==========================================
TEXT_COLS = ["title", "company_profile", "description", "requirements", "benefits"]
CAT_SRC   = ["employment_type", "required_experience", "required_education", "function", "industry"]
CAT_COLS  = CAT_SRC + ["country"]

BIN_COLS  = [
    "telecommuting", "has_company_logo", "has_questions", "has_salary",
    # "Missing section" flags: scam posts often leave these blank
    "no_company_profile", "no_requirements", "no_benefits", "no_department",
]

def prepare(df: pd.DataFrame) -> pd.DataFrame:
    """Same preparation for training data and for custom postings."""
    df = df.copy()
    for c in TEXT_COLS + CAT_SRC + ["salary_range", "department", "location"]:
        if c not in df:
            df[c] = ""
        df[c] = df[c].fillna("").astype(str)
    for c in ["telecommuting", "has_company_logo", "has_questions"]:
        if c not in df:
            df[c] = 0
        df[c] = df[c].fillna(0).astype(int)

    df["full_text"] = df[TEXT_COLS].agg(" ".join, axis=1)
    df["country"] = df["location"].str.split(",").str[0].str.strip()
    for c in CAT_COLS:
        df[c] = df[c].replace("", "Unknown")

    df["has_salary"]         = (df["salary_range"].str.strip() != "").astype(int)
    df["no_company_profile"] = (df["company_profile"].str.strip() == "").astype(int)
    df["no_requirements"]    = (df["requirements"].str.strip() == "").astype(int)
    df["no_benefits"]        = (df["benefits"].str.strip() == "").astype(int)
    df["no_department"]      = (df["department"].str.strip() == "").astype(int)
    return df

df = prepare(df_raw)
X = df[["full_text"] + CAT_COLS + BIN_COLS]
y = df["fraudulent"]

# ==========================================
# 3. STRATIFIED TRAIN-TEST SPLIT (same as before)
# ==========================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ==========================================
# 4. PIPELINE: binary text + one-hot categories + flags -> chi2 selection -> BernoulliNB
# ==========================================
preprocess = ColumnTransformer([
    ("text", CountVectorizer(
        binary=True, stop_words="english", ngram_range=(1, 2),
        min_df=5,            # drop very rare tokens (noise)
        max_df=0.9,          # drop tokens present in almost every post
        max_features=20000,
    ), "full_text"),
    ("cat", OneHotEncoder(handle_unknown="infrequent_if_exist", min_frequency=10), CAT_COLS),
    ("bin", "passthrough", BIN_COLS),
])

pipe = Pipeline(
    [
        ("pre", preprocess), 
        ("select", SelectKBest(chi2)), 
        ("nb", BernoulliNB())],
    memory="nb_cache",       # vectorise once per fold, not once per grid point
)

# BernoulliNB also learns from words that are ABSENT, so thousands of irrelevant
# features pile up evidence and push probabilities to 0/1. Keeping only the most
# discriminative features (chi2) and tuning alpha is what lifts precision.
param_grid = {
    "select__k": [300, 600, 1000, 2000, 4000],
    "nb__alpha": [0.01, 0.05, 0.1, 0.3, 1.0],
}
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

print("Tuning k and alpha (scored on PR-AUC)...")
grid = GridSearchCV(pipe, param_grid, scoring="average_precision", cv=cv, n_jobs=-1)

grid.fit(X_train, y_train)
# it will get best model
model = grid.best_estimator_
print(f"Best params: {grid.best_params_}  |  CV PR-AUC: {grid.best_score_:.4f}")


# ==========================================
# 5. THRESHOLD TUNING (on out-of-fold TRAIN predictions, never on test)
# ==========================================
TARGET_PRECISION = 0.60   # change to the precision you need

oof_prob = cross_val_predict(model, X_train, y_train, cv=cv, method="predict_proba", n_jobs=-1)[:, 1]
prec, rec, thr = precision_recall_curve(y_train, oof_prob)
prec, rec = prec[:-1], rec[:-1]

f1s = 2 * prec * rec / (prec + rec + 1e-12)
thr_best_f1 = thr[np.argmax(f1s)]

ok = np.where(prec >= TARGET_PRECISION)[0]
thr_target = thr[ok[0]] if len(ok) else thr_best_f1   # lowest threshold that hits the target = most recall kept

print(f"Threshold for best F1            : {thr_best_f1:.4f}")
print(f"Threshold for >= {TARGET_PRECISION:.0%} precision  : {thr_target:.4f}")
# exit(1)

# ==========================================
# 6. EVALUATION
# ==========================================
y_test_prob  = model.predict_proba(X_test)[:, 1]
y_train_prob = model.predict_proba(X_train)[:, 1]

print("\nTHRESHOLD COMPARISON ON TEST SET")
print(f"{'Threshold':<22}{'Precision':>10}{'Recall':>9}{'F1':>8}{'FP':>6}{'FN':>6}")
for name, t in [("Default 0.50", 0.5), ("Best F1", thr_best_f1), (f"Target {TARGET_PRECISION:.0%} prec", thr_target)]:
    p = (y_test_prob >= t).astype(int)
    tn_, fp_, fn_, tp_ = confusion_matrix(y_test, p).ravel()
    print(f"{name:<22}{precision_score(y_test, p, zero_division=0)*100:>9.2f}%"
          f"{recall_score(y_test, p)*100:>8.2f}%{f1_score(y_test, p)*100:>7.2f}%{fp_:>6}{fn_:>6}")

THRESHOLD = thr_best_f1     # switch to thr_target if precision matters more than recall

y_test_pred  = (y_test_prob  >= THRESHOLD).astype(int)
y_train_pred = (y_train_prob >= THRESHOLD).astype(int)

train_acc = accuracy_score(y_train, y_train_pred)
test_acc  = accuracy_score(y_test, y_test_pred)
tn, fp, fn, tp = confusion_matrix(y_test, y_test_pred).ravel()
cv_f1 = cross_val_score(model, X_train, y_train, cv=cv, scoring="f1").mean()  # at default 0.5

print(f"\nUSING THRESHOLD = {THRESHOLD:.4f}")
print("2. ACCURACY & OVERFITTING CHECK:")
print(f"   - Training Accuracy              : {train_acc * 100:.2f}%")
print(f"   - Testing Accuracy               : {test_acc * 100:.2f}%")
print(f"   - Balanced Accuracy (Imbalance)  : {balanced_accuracy_score(y_test, y_test_pred) * 100:.2f}%")
print(f"   - Overfitting Gap (Train - Test) : {(train_acc - test_acc) * 100:.2f}%\n")

print("3. FRAUD DETECTION EFFECTIVENESS (CLASS 1 METRICS):")
print(f"   - Precision (Flagged truly fake) : {precision_score(y_test, y_test_pred) * 100:.2f}%")
print(f"   - Recall / Sensitivity (Caught)  : {recall_score(y_test, y_test_pred) * 100:.2f}%")
print(f"   - Specificity (Real jobs passed) : {tn / (tn + fp) * 100:.2f}%")
print(f"   - F1-Score (Harmonic Mean)       : {f1_score(y_test, y_test_pred) * 100:.2f}% (5-Fold CV @0.5: {cv_f1 * 100:.2f}%)")
print(f"   - ROC-AUC Score                  : {roc_auc_score(y_test, y_test_prob):.4f}")
print(f"   - Precision-Recall AUC (PR-AUC)  : {average_precision_score(y_test, y_test_prob):.4f}\n")

print("4. CONFUSION MATRIX BREAKDOWN:")
print(f"   - True Negatives (Real -> Real)  : {tn}")
print(f"   - False Positives (False Alarms) : {fp} (FPR: {fp / (fp + tn) * 100:.2f}%)")
print(f"   - False Negatives (Missed Scams) : {fn}")
print(f"   - True Positives (Caught Scams)  : {tp}")
print("=" * 60)
print(classification_report(y_test, y_test_pred, target_names=["Real (0)", "Fake (1)"]))

# ==========================================
# 7. CUSTOM JOB POSTING PREDICTION
# ==========================================
def predict_job_posting(title, description, company_profile="", requirements="", benefits="",
                        telecommuting=0, has_company_logo=0, has_questions=0, has_salary=0,
                        employment_type="", required_experience="", required_education="",
                        function="", industry="", location="", department="",
                        threshold=None):
    threshold = THRESHOLD if threshold is None else threshold
    row = pd.DataFrame([{
        "title": title, "description": description, "company_profile": company_profile,
        "requirements": requirements, "benefits": benefits,
        "telecommuting": telecommuting, "has_company_logo": has_company_logo,
        "has_questions": has_questions, "salary_range": "x" if has_salary else "",
        "employment_type": employment_type, "required_experience": required_experience,
        "required_education": required_education, "function": function,
        "industry": industry, "location": location, "department": department,
    }])
    row = prepare(row)[["full_text"] + CAT_COLS + BIN_COLS]
    fake_prob = model.predict_proba(row)[0][1]
    verdict = "FAKE / SCAM" if fake_prob >= threshold else "REAL / LEGITIMATE"
    print("-" * 55)
    print(f"Job Title        : {title}")
    print(f"Fraud Probability: {fake_prob * 100:.2f}% (Threshold: {threshold * 100:.2f}%)")
    print(f"Verdict          : {verdict}")
    print("-" * 55)
    return fake_prob

print("\nTesting Custom Job Postings:")
predict_job_posting(
    title="Urgent Work From Home Data Entry Clerk - Earn $3500/Week",
    description="Immediate start! No experience required. Earn daily cash payouts from home processing simple forms. Send bank details for direct wire transfer setup.",
    requirements="Must have internet access and basic typing skills.",
    benefits="Daily cash bonuses, flexible hours.",
    telecommuting=1, has_company_logo=0, has_questions=0, has_salary=1,
)
predict_job_posting(
    title="Senior Python Backend Engineer",
    description="We are looking for an experienced backend engineer to design scalable REST APIs, optimize PostgreSQL queries, and maintain CI/CD pipelines.",
    company_profile="Founded in 2016, CloudScale builds enterprise infrastructure monitoring tools.",
    requirements="4+ years of experience with Python, Django or FastAPI, Docker, and AWS.",
    benefits="Health insurance, 401(k) matching, annual learning stipend.",
    telecommuting=0, has_company_logo=1, has_questions=1, has_salary=1,
    employment_type="Full-time", required_experience="Mid-Senior level",
    function="Engineering", industry="Computer Software", location="US, CA, San Francisco",
    department="Engineering",
)

