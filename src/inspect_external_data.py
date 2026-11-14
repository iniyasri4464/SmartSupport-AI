
import pandas as pd

# Load downloaded dataset
df = pd.read_csv("dataset/bitext_support.csv")

print("Dataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst Five Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nCategory Distribution:")
print(df["category"].value_counts())
