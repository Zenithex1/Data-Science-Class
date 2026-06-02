# 1) Even or Odd Checker

# Write a program that takes an integer and prints whether it is Even or Odd.
a = int(input("Enter your number: "))
b = int(input("Enter your number: "))

if a % 2 ==0:
    print("Even")
else:
    print("Odd")
# 2) Largest of Two Numbers

# Take two numbers as input and print the larger number.
if a>b:
    print(a)
else:
    print(b)

# 6) Login System (Simple)

# Store username = "admin" and password = "1234".
# Take input from user and print "Login Success" or "Login Failed"
user_name = "admin"
password = "1234"

user_input = input("Enter your username: ")
user_pass = input("Enter your password: ")

if user_input == user_name and password == user_pass:
    print("Login Success")
else:
    print("Login Failed")