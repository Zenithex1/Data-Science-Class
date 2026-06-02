# Python Practice Question (Difficulty 5/5 )

# You are given a dataset of customer purchases:

# purchases = [
#     ["Ram", 1200, "Completed", 2],
#     ["Shyam", 0, "Completed", 1],
#     ["Hari", 3400, "Pending", 3],
#     ["Sita", 2800, "Completed", 4],
#     ["Gita", -200, "Completed", 2],
#     ["Mina", 4500, "Completed", 5]
# ]

# Each item contains:

# [Customer_Name, Purchase_Amount, Status, Quantity]
# Task:

# Write a Python program that:

# Finds only valid purchases where:
# Purchase_Amount > 0
# Status == "Completed"
# Quantity > 0
# Store the customer names of valid purchases in a new list.
# Calculate:
# total number of valid purchases
# total revenue from valid purchases
# For each valid purchase:
# if amount is 4000 or more → "High Value Customer"
# if amount is between 2000 and 3999 → "Medium Value Customer"
# otherwise → "Low Value Customer"

purchases = [
    ["Ram", 1200, "Completed", 2],
    ["Shyam", 0, "Completed", 1],
    ["Hari", 3400, "Pending", 3],
    ["Sita", 2800, "Completed", 4],
    ["Gita", -200, "Completed", 2],
    ["Mina", 4500, "Completed", 5]
]
valid_customers =[]
total_valid = 0
total_revenue = 0

if purchases[0][1] > 0 and purchases[0][2] =='Completed' and purchases[0][3] > 0:
   valid_customers.append(purchases[0][0])
   total_valid += 1
   total_revenue += purchases[0][1]
   if purchases[0][1] > 4000:
      print("High Value Customer")
   elif purchases[0][1] > 2000 and  purchases[0][1] < 3999:
      print("Medium Value Customer")
   else:
      print("Low Value Customer")

if purchases[1][1] > 0 and purchases[1][2] =='Completed' and purchases[1][3] > 0:
      valid_customers.append(purchases[1][0])
      total_valid +=1
      total_revenue += purchases[1][1]
      if purchases[1][1] > 4000:
         print("High Value Customer")
      elif purchases[1][1] > 2000 and  purchases[1][1] < 3999:
         print("Medium Value Customer")
      else:
         print("Low Value Customer")

if purchases[2][1] > 0 and purchases[2][2] =='Completed' and purchases[2][3] > 0:
      valid_customers.append(purchases[2][0])
      total_valid +=1
      total_revenue += purchases[2][1]
      if purchases[2][1] > 4000:
         print("High Value Customer")
      elif purchases[2][1] > 2000 and  purchases[2][1] < 3999:
         print("Medium Value Customer")
      else:
       print("Low Value Customer")


if purchases[3][1] > 0 and purchases[3][2] == "Completed" and purchases[3][3] > 0:
    valid_customers.append(purchases[3][0])
    total_valid += 1
    total_revenue += purchases[3][1]

    if purchases[3][1] >= 4000:
        print(purchases[3][0], "High Value Customer")
    elif purchases[3][1] >= 2000:
        print(purchases[3][0], "Medium Value Customer")
    else:
        print(purchases[3][0], "Low Value Customer")


if purchases[4][1] > 0 and purchases[4][2] == "Completed" and purchases[4][3] > 0:
    valid_customers.append(purchases[4][0])
    total_valid += 1
    total_revenue += purchases[4][1]

    if purchases[4][1] >= 4000:
        print(purchases[4][0], "High Value Customer")
    elif purchases[4][1] >= 2000:
        print(purchases[4][0], "Medium Value Customer")
    else:
        print(purchases[4][0], "Low Value Customer")


if purchases[5][1] > 0 and purchases[5][2] == "Completed" and purchases[5][3] > 0:
    valid_customers.append(purchases[5][0])
    total_valid += 1
    total_revenue += purchases[5][1]

    if purchases[5][1] >= 4000:
        print(purchases[5][0], "High Value Customer")
    elif purchases[5][1] >= 2000:
        print(purchases[5][0], "Medium Value Customer")
    else:
        print(purchases[5][0], "Low Value Customer")


print("Valid Customers:", valid_customers)
print("Total Valid Purchases:", total_valid)
print("Total Revenue:", total_revenue)

print("============="*4)



# You are given a dataset of employee salary records:

# employees = [
#     ["Aarav", 50000, "Full-Time", 2],
#     ["Neha", 0, "Full-Time", 3],
#     ["Rohan", 75000, "Contract", 5],
#     ["Priya", 62000, "Full-Time", 0],
#     ["Suresh", -10000, "Full-Time", 4],
#     ["Anita", 90000, "Full-Time", 6]
# ]

# Each record contains:

# [Employee_Name, Salary, Employment_Type, Years_of_Experience]
# Task:
# 1. Identify valid employees where:
# Salary > 0
# Employment_Type == "Full-Time"
# Years_of_Experience > 0
# 2. Store valid employee names in a new list called:
# valid_employees
# 3. Calculate:
# total number of valid employees
# total salary of valid employees
# 4. Bonus Classification (for valid employees only):

# For each valid employee:

# if Salary >= 80000 → "High Salary Employee"
# if Salary >= 60000 and Salary < 80000 → "Mid Salary Employee"
# otherwise → "Low Salary Employee"

employees = [
    ["Aarav", 50000, "Full-Time", 2],
    ["Neha", 0, "Full-Time", 3],
    ["Rohan", 75000, "Contract", 5],
    ["Priya", 62000, "Full-Time", 0],
    ["Suresh", -10000, "Full-Time", 4],
    ["Anita", 90000, "Full-Time", 6]
]

valid_employee = []
total_valid_employee = 0
total_salary = 0

if employees[0][1] > 0 and employees[0][2] =="Full-Time" and employees[0][3] >0:
    valid_employee.append(purchases[0][0])
    total_valid_employee += 1
    total_salary += purchases[0][1]
    if purchases[0][1] >=80000:
        print("High Salary Employee")
    elif purchases[0][1] >=60000 and purchases[0][1] <80000:
        print("Mid Salary Employee")
    else:
        print("Low Salary Employee")

if employees[1][1] > 0 and employees[1][2] =="Full-Time" and employees[1][3] >0:
    valid_employee.append(purchases[1][0])
    total_valid_employee += 1
    total_salary += purchases[1][1]
    if purchases[1][1] >=80000:
        print("High Salary Employee")
    elif purchases[1][1] >=60000 and purchases[1][1] <80000:
        print("Mid Salary Employee")
    else:
        print("Low Salary Employee")

if employees[1][1] > 0 and employees[1][2] =="Full-Time" and employees[1][3] >0:
    valid_employee.append(purchases[1][0])
    total_valid_employee += 1
    total_salary += purchases[1][1]
    if purchases[1][1] >=80000:
        print("High Salary Employee")
    elif purchases[1][1] >=60000 and purchases[1][1] <80000:
        print("Mid Salary Employee")
    else:
        print("Low Salary Employee")

if employees[2][1] > 0 and employees[2][2] =="Full-Time" and employees[2][3] >0:
    valid_employee.append(purchases[2][0])
    total_valid_employee += 1
    total_salary += purchases[1][1]
    if purchases[2][1] >=80000:
        print("High Salary Employee")
    elif purchases[2][1] >=60000 and purchases[2][1] <80000:
        print("Mid Salary Employee")
    else:
        print("Low Salary Employee")

if employees[3][1] > 0 and employees[3][2] =="Full-Time" and employees[3][3] >0:
    valid_employee.append(purchases[3][0])
    total_valid_employee += 1
    total_salary += purchases[3][1]
    if purchases[3][1] >=80000:
        print("High Salary Employee")
    elif purchases[3][1] >=60000 and purchases[3][1] <80000:
        print("Mid Salary Employee")
    else:
        print("Low Salary Employee")

if employees[4][1] > 0 and employees[4][2] =="Full-Time" and employees[4][3] >0:
    valid_employee.append(purchases[4][0])
    total_valid_employee += 1
    total_salary += purchases[3][1]
    if purchases[4][1] >=80000:
        print("High Salary Employee")
    elif purchases[4][1] >=60000 and purchases[4][1] <80000:
        print("Mid Salary Employee")
    else:
        print("Low Salary Employee")


if employees[5][1] > 0 and employees[5][2] =="Full-Time" and employees[5][3] >0:
    valid_employee.append(purchases[5][0])
    total_valid_employee += 1
    total_salary += purchases[5][1]
    if purchases[5][1] >=80000:
        print("High Salary Employee")
    elif purchases[5][1] >=60000 and purchases[5][1] <80000:
        print("Mid Salary Employee")
    else:
        print("Low Salary Employee")


print(valid_employee)
print(f'The total valid employee is {total_valid_employee}')
print(f'The total_salary of valid employee is {total_salary}')