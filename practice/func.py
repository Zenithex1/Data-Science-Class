"""
9. Banking Transaction Logger

Create a function:

log_transaction(account_number, *transactions, **metadata)

Requirements:

Transactions are passed as:
("deposit", 5000)
("withdraw", 1200)
Metadata may include:
branch
employee_id
timestamp

Generate a transaction report.

Challenge: Calculate the final balance impact using only the transaction data.
"""

def log_transcation(account_number,*transactions,**metadata):
    print("======Transaction Report=========")
    print(f"The account_number is {account_number}")
    print("================="*2)
    print("======Transaction Detail==========")
    balance =0

    for process,amount in transactions:

        print(f"Process:{process}")
        print(f"Amount: {amount}")

        if process == "withdraw":
            balance -= amount
        elif process =="deposit":
            balance += amount
        else:
            print("Wrong data")
    print(f"the total balance after deposit is {balance}")
           
           
    print("================="*2)

    for k,j in metadata.items():
        print(f"{k}: {j}")
log_transcation(2020,("deposit",5000)  ,branch="Kathmandu",
    employee_id=101,
    timestamp="2026-06-17")
log_transcation(2020,("withdraw",6000)  ,branch="Kathmandu",
    employee_id=101,
    timestamp="2026-06-17")