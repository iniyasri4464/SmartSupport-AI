
import pandas as pd

# Load both datasets
original_df = pd.read_csv("dataset/complaints.csv")
external_df = pd.read_csv("dataset/complaints_external.csv")

# Combine datasets
combined_df = pd.concat(
    [original_df, external_df],
    ignore_index=True
)

# Remove duplicate complaints
combined_df = combined_df.drop_duplicates(
    subset=["complaint", "category"]
)

# Save combined dataset
combined_df.to_csv(
    "dataset/complaints_combined.csv",
    index=False
)

print("Combined Dataset Shape:", combined_df.shape)

print("\nCategory Distribution:")
print(combined_df["category"].value_counts())

print("\nCombined dataset saved successfully!")
