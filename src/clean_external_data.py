
import pandas as pd

# Load external dataset
df = pd.read_csv("dataset/bitext_support.csv")

# Keep only required columns
df = df[["instruction", "category"]]

# Rename columns for our project
df = df.rename(columns={
    "instruction": "complaint"
})

# Remove missing and duplicate records
df = df.dropna()
df = df.drop_duplicates()

# Convert complaint text to lowercase
df["complaint"] = df["complaint"].str.lower().str.strip()

# Save cleaned dataset
df.to_csv(
    "dataset/complaints_external.csv",
    index=False
)

print("Cleaned Dataset Shape:", df.shape)
print("\nCategory Distribution:")
print(df["category"].value_counts())

print("\nCleaned dataset saved successfully!")
