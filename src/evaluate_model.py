
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

# Load dataset
df = pd.read_csv("dataset/complaints.csv")

X = df["complaint"]
y = df["category"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# Load trained model and vectorizer
model = joblib.load("models/complaint_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

# Convert test text into numerical features
X_test_tfidf = vectorizer.transform(X_test)

# Predict categories
predictions = model.predict(X_test_tfidf)
print("\nActual vs Predicted:")

for actual, predicted in zip(y_test, predictions):
    print(f"Actual: {actual} | Predicted: {predicted}")

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy * 100, "%")

# Print precision, recall and F1-score
print("\nClassification Report:")
print(classification_report(y_test, predictions, zero_division=0))

# Display confusion matrix
cm = confusion_matrix(
    y_test,
    predictions,
    labels=model.classes_
)

print("Confusion Matrix:")
print(cm)

display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=model.classes_
)

display.plot(xticks_rotation=45)
