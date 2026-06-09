# Write a loop that prints the numbers from 10 down to 1, followed by the word "Blastoff!".

for i in range(10,0,-1):
    print(i)
print("Blastoff!")

print("===================="*2)
# Write a program that prints all multiples of 3 between 1 and 50.

for i in range(1,51):
    print(3*i)

print("===================="*2)

# Given a list of names, print a personalized greeting for each name (e.g., "Hello, Alice!").

name_list = ["jenish","alex","alish"]

for i in name_list:
    print("Hello, "+i)
print("===================="*2)

# Ask the user for a single word string, then print every character of that string on a new line, but in reverse order.

user_ask = input("Enter a string: ")
for i in user_ask[::-1]:
    print(i)

# Calculate the factorial of a given number $n$ (e.g., if $n = 5$, calculate $5 \times 4 \times 3 \times 2 \times 1$) using a loop.

n = int(input("Enter a number: "))
fac = 1
for i in range(1,6):
    fac = fac * i
print(fac)