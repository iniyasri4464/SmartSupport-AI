
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)
import matplotlib.pyplot as plt

# Load final dataset
df = pd.read_csv("dataset/final_complaints.csv")

X = df["complaint"]
y = df["category"]

# Use the same split as training
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# Load trained model
model = joblib.load("models/complaint_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

# Transform test data
X_test_tfidf = vectorizer.transform(X_test)

# Predict
predictions = model.predict(X_test_tfidf)

# Evaluation
print("Model Accuracy:",
      accuracy_score(y_test, predictions) * 100, "%")

print("\nClassification Report:")
print(classification_report(
    y_test,
    predictions,
    zero_division=0
))

# Confusion matrix
cm = confusion_matrix(
    y_test,
    predictions,
    labels=model.classes_
)

print("\nConfusion Matrix:")
print(cm)

display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=model.classes_
)

display.plot(xticks_rotation=45)
plt.tight_layout()
plt.show()
