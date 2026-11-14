
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# 1. Load dataset
df = pd.read_csv("dataset/final_complaints.csv")
X = df["complaint"]
y = df["category"]

# 2. Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# 3. Convert text into numerical values
vectorizer = TfidfVectorizer()

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# 4. Create and train model
model = LogisticRegression(
    max_iter=1000,
    class_weight="balanced"
)
model.fit(X_train_tfidf, y_train)

# 5. Make predictions
predictions = model.predict(X_test_tfidf)

# 6. Evaluate the model
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, predictions, zero_division=0))

# 7. Save trained model and vectorizer
joblib.dump(model, "models/complaint_model.pkl")
joblib.dump(vectorizer, "models/tfidf_vectorizer.pkl")

print("\nModel and vectorizer saved successfully!")
