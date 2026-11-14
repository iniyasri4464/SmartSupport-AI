
import pandas as pd

df = pd.read_csv("dataset/final_complaints.csv")

counts = df["category"].value_counts()

print("Category Percentages:")
print((counts / len(df) * 100).round(2))

print("\nMajority Category:")
print(counts.idxmax())

print("\nMinority Category:")
print(counts.idxmin())

print("\nImbalance Ratio:")
print(round(counts.max() / counts.min(), 2))
