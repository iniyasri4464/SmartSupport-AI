
import pandas as pd

# Load prepared datasets
bitext_df = pd.read_csv("dataset/complaints_prepared.csv")
it_df = pd.read_csv("dataset/it_support_english.csv")

# Combine datasets
final_df = pd.concat(
    [bitext_df, it_df],
    ignore_index=True
)

# Remove duplicates
final_df = final_df.drop_duplicates(
    subset=["complaint", "category"]
)

# Reset index
final_df = final_df.reset_index(drop=True)

# Save final dataset
final_df.to_csv(
    "dataset/final_complaints.csv",
    index=False
)

print("Final Dataset Shape:")
print(final_df.shape)

print("\nFinal Category Distribution:")
print(final_df["category"].value_counts())

print("\nMissing Values:")
print(final_df.isnull().sum())

print("\nFinal dataset saved successfully!")
