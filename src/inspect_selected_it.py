
import pandas as pd

df = pd.read_csv("dataset/it_support_selected.csv")

print("Dataset Shape:")
print(df.shape)

print("\nFirst 20 Complaints:")
for i, complaint in enumerate(df["complaint"].head(20), start=1):
    print(f"{i}. {complaint}")

print("\nCategory Distribution:")
print(df["category"].value_counts())
