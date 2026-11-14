
import pandas as pd

# Load IT support dataset
df = pd.read_parquet("dataset/it_support_train.parquet")

# Select categories that fit our project
selected_df = df[df["label"].isin([0, 1, 5])].copy()

# Map labels to our project categories
category_mapping = {
    0: "Account",
    1: "Technical",
    5: "Technical"
}

selected_df["category"] = selected_df["label"].map(category_mapping)

# Keep only required columns
selected_df = selected_df[["text", "category"]]

# Rename text column
selected_df = selected_df.rename(
    columns={"text": "complaint"}
)

# Remove missing and duplicate records
selected_df = selected_df.dropna()
selected_df = selected_df.drop_duplicates(
    subset=["complaint", "category"]
)

# Save selected dataset
selected_df.to_csv(
    "dataset/it_support_selected.csv",
    index=False
)

print("Selected Dataset Shape:", selected_df.shape)

print("\nCategory Distribution:")
print(selected_df["category"].value_counts())

print("\nSelected dataset saved successfully!")
