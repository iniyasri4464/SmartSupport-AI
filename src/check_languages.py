
import pandas as pd
from langdetect import detect, LangDetectException

df = pd.read_csv("dataset/it_support_selected.csv")

def detect_language(text):
    try:
        return detect(str(text))
    except LangDetectException:
        return "unknown"

df["language"] = df["complaint"].apply(detect_language)

print("Language Distribution:")
print(df["language"].value_counts())

print("\nSample English Complaints:")
print(
    df[df["language"] == "en"]["complaint"]
    .head(10)
    .to_string(index=False)
)
