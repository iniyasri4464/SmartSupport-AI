
import joblib
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR / "src"))

from recommendations import get_solution

# Load trained model and vectorizer
model = joblib.load(
    BASE_DIR / "models" / "complaint_model.pkl"
)

vectorizer = joblib.load(
    BASE_DIR / "models" / "tfidf_vectorizer.pkl"
)

# Fresh complaints not added to training data
complaints = [
    "My wifi disconnects whenever I join an online meeting",
    "The internet speed is extremely slow in my office",
    "I was charged twice for the same monthly subscription",
    "My payment was deducted but the invoice is still unpaid",
    "I cannot access my employee login account",
    "Please unlock my account after multiple failed logins",
    "The shopping package has not arrived on the promised date",
    "I received the wrong item in my delivery",
    "My laptop screen freezes whenever I open the application",
    "The printer is showing an error when I try to print"
]

print("SMART SUPPORT AI - FRESH TESTING")

for i, complaint in enumerate(complaints, start=1):

    complaint_tfidf = vectorizer.transform([complaint])

    prediction = model.predict(complaint_tfidf)[0]

    probabilities = model.predict_proba(complaint_tfidf)[0]
    confidence = max(probabilities) * 100

    solution = get_solution(prediction)

    print("\n--------------------------------")
    print(f"Test Case: {i}")
    print("Complaint:", complaint)
    print("Predicted Category:", prediction)
    print(f"Prediction Score: {confidence:.2f}%")
    print("Recommended Solution:", solution)
