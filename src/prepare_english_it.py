import pandas as pd
from langdetect import DetectorFactory
DetectorFactory.seed = 0

df = pd.read_csv("dataset/it_support_selected.csv")

# Detect English complaints
from langdetect import detect, LangDetectException

def detect_language(text):
    try:
        return detect(str(text))
    except LangDetectException:
        return "unknown"

df["language"] = df["complaint"].apply(detect_language)

# Keep English complaints only
english_df = df[df["language"] == "en"].copy()

# Remove language column
english_df = english_df[["complaint", "category"]]

# Remove duplicates
english_df = english_df.drop_duplicates(
    subset=["complaint", "category"]
)

# Save final English IT dataset
english_df.to_csv(
    "dataset/it_support_english.csv",
    index=False
)

print("English Dataset Shape:")
print(english_df.shape)

print("\nCategory Distribution:")
print(english_df["category"].value_counts())

print("\nEnglish IT dataset saved successfully!")
