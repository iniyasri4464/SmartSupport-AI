
import pandas as pd

df = pd.read_csv("dataset/final_complaints.csv")

# Check repeated complaint text
duplicate_text = df[
    df.duplicated(subset=["complaint"], keep=False)
]

print("Total Records:", len(df))

print("\nRepeated Complaint Records:",
      len(duplicate_text))

# Check complaints assigned to multiple categories
conflicts = (
    df.groupby("complaint")["category"]
    .nunique()
)

conflicts = conflicts[conflicts > 1]

print("\nConflicting Complaint Texts:",
      len(conflicts))

print("\nExamples of Conflicting Complaints:")
for complaint in conflicts.index[:10]:
    print("\nComplaint:", complaint)
    print(
        df[df["complaint"] == complaint][
            ["complaint", "category"]
        ].to_string(index=False)
    )
