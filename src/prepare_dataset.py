
import pandas as pd

df = pd.read_csv("dataset/complaints_combined.csv")

# Map external categories to our project categories
category_mapping = {
    "ACCOUNT": "Account",
    "ORDER": "Order",
    "DELIVERY": "Order",
    "SHIPPING": "Order",
    "CANCEL": "Order",
    "REFUND": "Billing",
    "INVOICE": "Billing",
    "PAYMENT": "Billing",
    "SUBSCRIPTION": "Billing"
}

df["category"] = df["category"].replace(category_mapping)

# Remove categories that don't fit our five-class project
df = df[df["category"].isin([
    "Network",
    "Billing",
    "Account",
    "Technical",
    "Order"
])]

df.to_csv("dataset/complaints_prepared.csv", index=False)

print("Prepared Dataset Shape:", df.shape)
print("\nFinal Category Distribution:")
print(df["category"].value_counts())

print("\nPrepared dataset saved successfully!")

original_df = pd.read_csv("dataset/complaints.csv")

print("\nOriginal Dataset Distribution:")
print(original_df["category"].value_counts())