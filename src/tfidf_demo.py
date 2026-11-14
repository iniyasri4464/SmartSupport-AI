
from sklearn.feature_extraction.text import TfidfVectorizer

complaints = [
    "my internet is very slow",
    "my wifi is not working",
    "I need a refund for my payment",
    "my bill amount is incorrect"
]

vectorizer = TfidfVectorizer()

# Learn vocabulary
vectorizer.fit(complaints)

# Convert text into numbers
tfidf_matrix = vectorizer.transform(complaints)

print("Vocabulary:")
print(vectorizer.get_feature_names_out())

print("\nNumerical representation:")
print(tfidf_matrix.toarray())
