from sklearn.metrics import make_scorer, precision_score
import pandas as pd

from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Load dataset
df = pd.read_csv("dataset/final_complaints.csv")

X = df["complaint"]
y = df["category"]

# Create a pipeline
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("model", LogisticRegression(
        max_iter=1000,
        class_weight="balanced"
    ))
])

# 4-fold stratified cross-validation
cv = StratifiedKFold(
    n_splits=4,
    shuffle=True,
    random_state=42
)

# Evaluate model
scores = cross_validate(
    pipeline,
    X,
    y,
    cv=cv,
    scoring={
        "accuracy": "accuracy",
        "precision_macro": make_scorer(
            precision_score,
            average="macro",
            zero_division=0
        ),
        "recall_macro": "recall_macro",
        "f1_macro": "f1_macro"
    }
)

print("Cross Validation Results:")

print("\nAccuracy:",
      scores["test_accuracy"])

print("\nMean Accuracy:",
      scores["test_accuracy"].mean() * 100, "%")

print("\nMean Precision:",
      scores["test_precision_macro"].mean())

print("\nMean Recall:",
      scores["test_recall_macro"].mean())

print("\nMean F1 Score:",
      scores["test_f1_macro"].mean())
