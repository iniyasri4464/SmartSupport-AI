
import joblib

# Load the saved model and vectorizer
model = joblib.load("models/complaint_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

# Get complaint from user
complaint = input("Enter your complaint: ")

# Convert complaint into numerical form
complaint_vector = vectorizer.transform([complaint])

# Predict category
prediction = model.predict(complaint_vector)

print("Predicted Category:", prediction[0])
