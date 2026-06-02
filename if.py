# 2. ATM Withdrawal Security Check

# Create a program that asks the user for:

# Card inserted? (yes/no)
# PIN correct? (yes/no)
# Account balance
# Withdrawal amount

# Rules:

# If card is inserted:
# If PIN is correct:
# If balance is greater than withdrawal amount:
# If withdrawal amount is divisible by 100:
# Print "Transaction Successful"
# Else:
# Print "Enter amount in multiples of 100"
# Else:
# Print "Insufficient Balance"
# Else:
# Print "Incorrect PIN"
# Else:
# Print "Insert Card First"

# card_inserted = (input("Is the card inserted(Yes/No): ")).lower()
# pin_correct = input("Is the pin correct((Yes/No)): ").lower()
# account_balance = int(input("What is the account balance?: "))
# withdrawal_amount = int(input("How much do you want to widthdraw?: "))

# if card_inserted == "yes":
#     if pin_correct == "yes":
#         if account_balance > withdrawal_amount:
#             if withdrawal_amount % 100 == 0:
#                 print("Transaction Successful")
#             else:
#                 print("Enter amount in multiples of 100")
#         else:
#             print("Insufficient Balance")
#     else:
#         print("Incorrect Pin")
# else:
#     print("Insert Card First")

print("-----------------" * 3)

# 3. Online Food Delivery Checker

# Write a program that asks for:

# User membership type (gold/silver/normal)
# Order amount
# Distance in km

# Rules:

# If membership is "gold":
# If order amount is above 500:
# Free delivery
# Else:
# Delivery charge = 50
# Else if membership is "silver":
# If order amount is above 1000:
# Free delivery
# Else:
# If distance is more than 10 km:
# Delivery charge = 100
# Else:
# Delivery charge = 60
# Else:
# If order amount is above 2000:
# Free delivery
# Else:
# Delivery charge = 150

# Finally print:

# Membership type
# Final delivery charge


user_membership = input("Enter your membership  (Gold,Silver,normal): ").lower()
order_amount = int(input("Enter your order amount: "))
distance = int(input("Enter you distance in km: "))
if user_membership == "gold":
    if order_amount > 500:
        print("Free delivery")
    else:
        delivery_charge = 50
    

elif user_membership == "silver":
    if order_amount > 1000:
        print("Free Delivery")
    else:
        if distance > 10:
            delivery_charge = 100
            print(f'Your membership is : {user_membership}')
            print(f'Your delivery_charge is : {delivery_charge}')

        else:
            delivery_charge = 60
            print(f'Your membership is : {user_membership}')
            print(f'Your delivery_charge is : {delivery_charge}')


else:
    if order_amount > 2000:
        print("free Delivery")
    else:

        delivery_charge = 150
        print(f'Your membership is : {user_membership}')
        print(f'Your delivery_charge is : {delivery_charge}')

print("========="*3)

user_membership = input("Enter your membership  (Gold,Silver,normal): ").lower()
order_amount = int(input("Enter your order amount: "))
distance = int(input("Enter you distance in km: "))
delivery_charge = 0
if user_membership == "gold":
    if order_amount > 500:
        print("Free delivery")
    else:
        delivery_charge = 50
    
elif user_membership == "silver":
    if order_amount > 1000:
        print("Free Delivery")
    else:
        if distance > 10:
            delivery_charge = 100
   

        else:
            delivery_charge = 60
         
else:
    if order_amount > 2000:
        print("free Delivery")
    else:

        delivery_charge = 150
        
print(f'Your membership is : {user_membership}')
print(f'Your delivery_charge is : {delivery_charge}')

