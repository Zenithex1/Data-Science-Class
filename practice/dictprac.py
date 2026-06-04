# High-Difficulty Python Practice Questions (Data Analyst Focus)
# 1. Customer Filtering

# You are given:

# customers = [
#     {"name": "Ram", "age": 25, "purchase": 1500},
#     {"name": "Sita", "age": 40, "purchase": 8000},
#     {"name": "Hari", "age": 35, "purchase": 500},
#     {"name": "Gita", "age": 29, "purchase": 3000}
# ]

# Find all customers whose age is between 25 and 40 (inclusive) and whose purchase amount is greater than 1000 and print it in a list.


customers = [
    {"name": "Ram", "age": 25, "purchase": 1500},
    {"name": "Sita", "age": 40, "purchase": 8000},
    {"name": "Hari", "age": 35, "purchase": 500},
    {"name": "Gita", "age": 29, "purchase": 3000}
]
required_customers = []

if customers[0]['age'] >=25 and customers[0]['age']<=40 and customers[0]['purchase'] > 1000:
    required_customers.append(customers[0]['name'])
if customers[1]['age'] >=25 and customers[1]['age']<=40 and customers[1]['purchase'] > 1000:
    required_customers.append(customers[1]['name'])

if customers[2]['age'] >=25 and customers[2]['age']<=40 and customers[2]['purchase'] > 1000:
    required_customers.append(customers[2]['name'])

if customers[3]['age'] >=25 and customers[3]['age']<=40 and customers[3]['purchase'] > 1000:
    required_customers.append(customers[3]['name'])

print(required_customers)





# 2. Transaction Risk Detection
# transactions = [
#     {"id": 1, "amount": 12000, "verified": False},
#     {"id": 2, "amount": 5000, "verified": True},
#     {"id": 3, "amount": 15000, "verified": True},
#     {"id": 4, "amount": 25000, "verified": False}
# ]


# Identify all suspicious transactions using logical operators and conditions.


transactions = [
    {"id": 1, "amount": 12000, "verified": False},
    {"id": 2, "amount": 5000, "verified": True},
    {"id": 3, "amount": 15000, "verified": True},
    {"id": 4, "amount": 25000, "verified": False}
]

if transactions[0]['verified'] == True and transactions[0]['amount'] <= 20000:
    print("Transaction processed")
else:
    print("Suspicious Transaction")
if transactions[1]['verified'] == True and transactions[1]['amount'] <= 20000:
    print("Transaction processed")
else:
    print("Suspicious Transaction")
if transactions[2]['verified'] == True and transactions[2]['amount'] <= 20000:
    print("Transaction processed")
else:
    print("Suspicious Transaction")
if transactions[3]['verified'] == True and transactions[3]['amount'] <= 20000:
    print("Transaction processed")
else:
    print("Suspicious Transaction")


print("====================="*3)

# 3. Product Revenue Analysis
# sales = {
#     "Laptop": 120000,
#     "Mouse": 15000,
#     "Keyboard": 25000,
#     "Monitor": 70000
# }

# Find the product with the highest revenue without using max().

sales = {
    "Laptop": 120000,
    "Mouse": 15000,
    "Keyboard": 25000,
    "Monitor": 70000
}



if sales['Keyboard'] > sales['Laptop'] and sales['Keyboard'] > sales['Mouse'] and sales['Keyboard'] > sales['Monitor'] :
    print(f'Keyboard is the highest amount')
elif  sales['Laptop'] > sales['Keyboard'] and sales['Laptop'] > sales['Mouse'] and sales['Laptop'] > sales['Monitor'] :
    print(f'Laptop is the highest amount')
elif sales['Mouse'] > sales['Keyboard'] and sales['Mouse'] > sales['Laptop'] and sales['Mouse'] > sales['Monitor'] :
     print(f'Mouse is the highest amount')
elif sales['Monitor'] > sales['Keyboard'] and sales['Monitor'] > sales['Laptop'] and sales['Monitor'] > sales['Keyboard'] :
         print(f'Monitor is the highest amount')

print("==============="*4)
# 4. Employee Bonus Eligibility
# employees = [
#     {"name": "A", "experience": 5, "rating": 4.8},
#     {"name": "B", "experience": 2, "rating": 4.9},
#     {"name": "C", "experience": 7, "rating": 4.1},
#     {"name": "D", "experience": 10, "rating": 4.7}
# ]

# Determine which employees are eligible for a bonus based on experience and rating criteria.

employees = [
    {"name": "A", "experience": 5, "rating": 4.8},
    {"name": "B", "experience": 2, "rating": 4.9},
    {"name": "C", "experience": 7, "rating": 4.1},
    {"name": "D", "experience": 10, "rating": 4.7}
]

if employees[0]['experience'] >=5 and employees[0]['rating'] >= 4.75:
    print(f'{employees[0]['name']} is eligible for bonus')
else:
    print(f"Not eligible for bonus")
if employees[1]['experience'] >=5 and employees[1]['rating'] >= 4.75:
    print(f'{employees[1]['name']} is eligible for bonus')
else:
    print(f"Not eligible for bonus")
if employees[2]['experience'] >=5 and employees[2]['rating'] >= 4.75:
    print(f'{employees[2]['name']} is eligible for bonus')
else:
    print(f"Not eligible for bonus")
if employees[3]['experience'] >=5 and employees[3]['rating'] >= 4.75:
    print(f'{employees[3]['name']} is eligible for bonus')
else:
    print(f"Not eligible for bonus")
# 5. Inventory Monitoring
# inventory = {
#     "Apple": 5,
#     "Banana": 20,
#     "Orange": 3,
#     "Mango": 15
# }

# Generate a list of products that need restocking.

inventory = {
    "Apple": 5,
    "Banana": 20,
    "Orange": 3,
    "Mango": 15
}

restock_items = []
if inventory['Apple'] < 5 :
    restock_items= inventory.pop('Apple')

print(restock_items)
    

# 6. Data Quality Audit
# data = [45, -2, 78, 0, 15, -8, 99]

# Count positive values, negative values, and zeros.

data = [45, -2, 78, 0, 15, -8, 99]
count_positive = 0
count_zero = 0
count_negative = 0
if data[0] > 0:
    count_positive += 1
elif data[0] == 0:
    count_zero += 1
elif data[0] < 0:
    count_negative += 1

if data[1] > 0:
    count_positive += 1
elif data[1] == 0:
    count_zero += 1
elif data[1] < 0:
    count_negative += 1

if data[2] > 0:
    count_positive += 1
elif data[2] == 0:
    count_zero += 1
elif data[2] < 0:
    count_negative += 1

if data[3] > 0:
    count_positive += 1
elif data[3] == 0:
    count_zero += 1
elif data[3] < 0:
    count_negative += 1

if data[4] > 0:
    count_positive += 1
elif data[4] == 0:
    count_zero += 1
elif data[4] < 0:
    count_negative += 1    

if data[5] > 0:
    count_positive += 1
elif data[5] == 0:
    count_zero += 1
elif data[5] < 0:
    count_negative += 1 

if data[6] > 0:
    count_positive += 1
elif data[6] == 0:
    count_zero += 1
elif data[6] < 0:
    count_negative += 1 



print(f'The number of negative number:{count_negative}')
print(f'The number of zero number:{count_zero}')
print(f'The number of positive number:{count_positive}')

