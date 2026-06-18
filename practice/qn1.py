"""
1. Banking Analytics Engine (Multi-Customer System)

You are building a banking analytics system.

Data format:

Each customer:

{
    "name": "Aarav",
    "age": 28,
    "balance": 10000,
    "transactions": [
        ("deposit", 5000),
        ("withdraw", 2000)
    ]
}
Tasks:
Store multiple customers in a list
Write a function to:
process all transactions
update balance
classify customer:
High Value → balance > 15000
Medium → 8000–15000
Low → < 8000
Extra challenge:
Find:
highest balance customer
total money deposited across all customers
total money withdrawn across all customers
"""
# customers = [
#     {
#         "name": "Aarav",
#         "age": 28,
#         "balance": 10000,
#         "transactions": [
#             ("deposit", 5000),
#             ("withdraw", 2000)
#         ]
#     },
#     {
#         "name": "Rita",
#         "age": 25,
#         "balance": 8000,
#         "transactions": [
#             ("deposit", 3000),
#             ("withdraw", 1000)
#         ]
#     }
# ]
# def transaction():
#     for customer in customers:
#         balance =customer['balance'] 

# transaction()

# 2. Fraud Detection System (Real-world Logic)

# You are given transaction logs:

# ("Aarav", "deposit", 5000)
# ("Aarav", "withdraw", 20000)
# ("Rita", "withdraw", 1000)
# Tasks:
# Use a dictionary to track balances per user
# Apply rules:
# deposit adds balance
# withdraw subtracts balance
# Detect fraud if:
# withdraw > current balance → "FRAUD ALERT"
# negative transaction amount → "INVALID"

transactions = [
    ("Aarav", "deposit", 5000),
    ("Aarav", "withdraw", 20000),
    ("Rita", "withdraw", 1000),
    ("John", "deposit", -500)
]

balances = {}
fraud_reports = []

for name, transaction_type, amount in transactions:

    if amount < 0:
        print(f"INVALID: {name} has a negative transaction amount ({amount})")
        fraud_reports.append(name)
        continue

    if name not in balances:
        balances[name] = 0

    if transaction_type == "deposit":
        balances[name] += amount

    elif transaction_type == "withdraw":

        if amount > balances[name]:
            print(f"FRAUD ALERT: {name} tried to withdraw {amount}")
            fraud_reports.append(name)
        else:
            balances[name] -= amount

    else:
        print(f"Unknown transaction type: {transaction_type}")

print("\n===== FINAL BALANCES =====")
for name, balance in balances.items():
    print(f"{name}: {balance}")

print("\n===== FRAUD REPORT =====")
for person in fraud_reports:
    print(person)