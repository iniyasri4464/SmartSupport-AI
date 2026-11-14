
import pandas as pd

# Load the dataset
df = pd.read_csv("dataset/complaints.csv")

# Display first five rows
print("First five complaints:")
print(df.head())

# Display dataset shape
print("\nDataset shape:")
print(df.shape)

# Display category counts
print("\nCategory distribution:")
print(df["category"].value_counts())

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())
