# Type Casting

a = 1
print(type(a))

a = "Hello"
b = str(a)
print(type(a))

print(type)

a = "10"
print(int(a))
a = "Hello"
# print(int(a))

a = 1
print(bool(a))
print(type(a))

a = "10"
b = "20"
print(int(a) + int(b))

# Comparision Operator
print(1 == 1)
print("hari" == "hari")
print(1 != 0)
print(5 <= 2)
print(13 >= 1)

print(5 >= 5)
b = 2
a = 20
print(b > a)
print(a >= 20)
print("==========" * 2)

# Logical Operator
print("Logical Operator Output")

print(1 == 1 and 5 > 2)
print(False and True)

print(True or False)
print(False or True)

print(not (True))
print("==========" * 2)

# String

Data = "TEST okay"
data = "213"
print(Data.lower())
print(Data.title())  # Turns first letter capital of every word
print(Data.upper())
print(len(Data))
print(Data[0:2])
print(data.isdigit())
print(not (data.isalpha()))

a = "Jenish , SHrestha"
b = a.split(",")
print(b)

c = "nom"

print(c.capitalize())  # Turns first letter of first word

name = input("Enter your first name")
lname = input("Enter your last name")
age = int(input("Enter your age"))
print("my name is ", name, lname, "I am ", age, "years old.")

# String formatting

print(f"My name is {name} {lname} and my age is {age+2-2} .")
print("==========" * 2)

# input
# user input is always string
name = input(f"Enter Your name : ")
print(f"Your name is {name} and type is {type(name)}")
