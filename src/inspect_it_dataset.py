
import pandas as pd

# Load IT support dataset
df = pd.read_parquet("dataset/it_support_train.parquet")

print("Dataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 5 Records:")
print(df.head().to_string())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nData Types:")
print(df.dtypes)

print("\nLabel Distribution:")
print(df["label"].value_counts().sort_index())

print("\nCategory-wise label mapping:")

label_names = {
    0: "Active Directory",
    1: "Computer-Services",
    2: "EOL",
    3: "Fileservice",
    4: "O365",
    5: "Software",
    6: "Support general"
}

for label, count in df["label"].value_counts().sort_index().items():
    print(f"{label} - {label_names[label]}: {count}")


print("\nSample complaints by label:")

for label in sorted(df["label"].unique()):
    print(f"\n--- Label {label} ---")

    samples = df[df["label"] == label]["text"].head(5)

    for complaint in samples:
        print("-", complaint)
for label in [0, 1]:
    print(f"\n--- Label {label} ---")

    samples = df[df["label"] == label]["text"].head(15)

    for complaint in samples:
        print("-", complaint)