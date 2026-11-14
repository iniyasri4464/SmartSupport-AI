from recommendations import get_solution

tests = [
    ("Billing", "I was charged twice for my subscription"),
    ("Account", "My account is locked"),
    ("Order", "My order has not arrived"),
    ("Network", "My wifi keeps disconnecting"),
    ("Technical", "My laptop application keeps freezing")
]

for category, complaint in tests:
    print("\nComplaint:", complaint)
    print("Category:", category)
    print("Recommendation:", get_solution(category, complaint))