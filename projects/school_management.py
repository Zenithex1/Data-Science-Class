# Here you go — one big question, copy it and attempt it fully:

# ---

# ## The Smart School Management System

# **Scenario:** You are building a Python program for a school. The school wants to manage students, teachers, subjects, grades, and fees. Build the entire system step by step inside one program.

# ---

# ### The Question

# **1. Create the data**

# Create the following variables:
# - School name (string), total_students (int), passing_percentage (float), is_government_school (bool)
# - A tuple called `school_info` storing: school name, city, year established — this should never change
# - A set called `available_subjects` with at least 6 subjects (some duplicates included — let the set handle it)

# ---

# **2. Create students**

# Create a list of 5 student dictionaries. Each student dictionary must have:
# - `name`, `age`, `grade` (A/B/C/D), `marks` (a list of 5 subject marks), `fees_paid` (True/False)

# Example structure:
# ```python
# students = [
#     {"name": "Aisha", "age": 15, "grade": "A", "marks": [88, 92, 75, 95, 80], "fees_paid": True},
#     ...
# ]
# ```

# ---

# **3. Create teachers**

# Create a list of 3 teacher dictionaries, each with:
# - `name`, `subject`, `experience_years`, `is_senior` (True if experience >= 5)

# ---

# **4. Filter using conditions**

# Using if/elif/else and logical/comparison operators:
# - (a) Loop through students and print only those who have **fees paid AND average marks above 80**
# - (b) Loop through students and assign a result:
#   - Average >= 85 → "Distinction"
#   - Average >= 60 → "Pass"
#   - else → "Fail"
# - (c) Print only senior teachers (experience >= 5 years)

# ---

# **5. Write these functions**

# ```python
# # Function 1
# def calculate_average(marks):
#     # takes a list of marks
#     # returns the average (rounded to 2 decimal places)

# # Function 2
# def get_top_student(students):
#     # loops through all students
#     # returns the name of the student with highest average marks

# # Function 3
# def count_passed_students(students, passing_mark=60):
#     # counts how many students have average marks above passing_mark
#     # passing_mark has a default value of 60
#     # returns the count

# # Function 4
# def apply_fee_discount(fee, is_government_school, is_senior_student):
#     # if government school → 20% discount
#     # if senior student (age >= 16) → additional 10% discount
#     # return final fee after discounts
# ```

# ---

# **6. Use loops**

# - (a) Use a **for loop** to print each student's name, their average marks (use your function), and their result (Distinction / Pass / Fail)
# - (b) Use a **while loop** to simulate a fee collection counter — keep collecting fees from students one by one (pop from a list of unpaid students) until everyone has paid, printing a message each time
# - (c) Use a **for loop** with `enumerate` to print a numbered list of all available subjects

# ---

# **7. Build the Student class**

# ```python
# class Student:
#     # __init__ takes: name, age, marks (list), fees_paid (bool)
    
#     def get_average(self):
#         # returns average of marks
    
#     def get_result(self):
#         # returns "Distinction", "Pass", or "Fail" based on average
    
#     def get_profile(self):
#         # prints everything about the student neatly:
#         # name, age, average, result, fee status
# ```

# - Create 3 Student objects using this class
# - Call `get_profile()` on each one
# - Store all 3 in a list and loop through them calling `get_profile()`

# ---

# **8. Final summary report**

# At the end of your program, print a report like this using all your functions and data:

# ```
# ===== SCHOOL REPORT =====
# School: Greenwood High  |  City: Mumbai
# Total Students: 5
# Top Student: Aisha (avg: 86.0)
# Students Passed: 4
# Students Failed: 1
# Senior Teachers: 2
# Subjects Offered: {'Math', 'Science', 'English', 'History', 'PE', 'Art'}
# =========================
# ```

# ---

# ### Rules
# - Write everything in **one single Python file**
# - Do **not** look at notes for the basic stuff — only look if truly stuck
# - Use your functions inside the class wherever possible
# - All output should be clean and readable

# ---

# ### Hint (only read if stuck)
# - Start from top to bottom — data first, then functions, then class, then loops, then report
# - Your `calculate_average()` function can be called inside the class `get_average()` method — functions and classes can work together
# - For the while loop in step 6b, first make a new list of only students where `fees_paid == False`, then pop from it

school_name = "Ideal"
total_students = 500
passing_percentage = 80
is_government_school = True
school_detail = ("Ideal","Kathmandu",2020)

available_subjects ={"Science","English","Computer","Computer","Math","DSA"}

students = [
    {
        "name": "Jenish",
        "age": 22,
        "grade": "A",
        "marks": [30, 20, 30, 10, 20],
        "fees_paid": True
    },
    {
        "name": "Ram",
        "age": 21,
        "grade": "B",
        "marks": [25, 30, 20, 15, 18],
        "fees_paid": False
    },
    {
        "name": "Sita",
        "age": 20,
        "grade": "A",
        "marks": [35, 28, 32, 30, 25],
        "fees_paid": True
    },
    {
        "name": "Hari",
        "age": 22,
        "grade": "C",
        "marks": [20, 15, 18, 22, 19],
        "fees_paid": False
    },
    {
        "name": "Gita",
        "age": 21,
        "grade": "B",
        "marks": [28, 24, 26, 29, 30],
        "fees_paid": True
    }
]

teachers = [
    {
        "name": "Alex",
        "subject": "Math",
        "experience_years": 14,
        "is_senior": True
    },
    {
        "name": "Jen",
        "subject": "Computer",
        "experience_years": 3,
        "is_senior": False
    },
    {
        "name": "Axel",
        "subject": "DSA",
        "experience_years": 8,
        "is_senior": True
    }
]
for student in students:
        avg = (sum(student["marks"])/len(student["marks"]))
        if student["fees_paid"] ==True and  avg >= 10:
            if avg >= 85 :
                  print("Distinction")
            elif avg >=60:
                  print("Pass")
            else:
                  print("Fail")

for teacher in teachers:
      if teacher["experience_years"] >= 5:
            print(teacher)
    

def calculate_average(marks):
     avg = round(sum(marks)/len(marks),2)
     return avg

def get_top_students(students):
    top_student = students[0]
    for student in students:
          if sum(student["marks"])/len(student)> sum(top_student["marks"])/len(student):
                top_student=student
    return top_student["name"]

def count_passed_students(students,passing_mark=60):
    passing_count = 0
    for student in students:
        if sum(student["marks"])/len(student["marks"]) >= 60:
             passing_count += 1
    return f'Total no of passing student :{passing_count}'

def apply_fee_discount(fee,is_government_school,is_senior_student):
     if is_government_school:
        fee -= (20/100)*fee
        for student in students:
          if student["age"] >= 16 and is_senior_student :
               fee -= (10/100)*fee
        
        return fee
     
for student in students:
     print(f'Name: {student["name"]}')
     print(calculate_average(student["marks"]))
     if student["grade"] == 'A':
          print("Distinction")
     elif student["grade"] == 'B' or student["grade"] == 'B':
          print("Pass")
     else:
          print("Fail")
     print("======================")

print("=========================")
                
print(apply_fee_discount(1000,True,True))
print("======================"*3)
print(calculate_average([50,60,70,50,30]))
print(count_passed_students(
      [
    {
        "name": "Jenish",
        "age": 22,
        "grade": "A",
        "marks": [30, 20, 30, 10, 20],
        "fees_paid": True
    },
    {
        "name": "Ram",
        "age": 21,
        "grade": "B",
        "marks": [75, 70, 70, 85, 98],
        "fees_paid": False
    },
    {
        "name": "Sita",
        "age": 20,
        "grade": "A",
        "marks": [35, 28, 32, 30, 25],
        "fees_paid": True
    },
    {
        "name": "Hari",
        "age": 22,
        "grade": "C",
        "marks": [20, 15, 18, 22, 19],
        "fees_paid": False
    },
    {
        "name": "Gita",
        "age": 21,
        "grade": "B",
        "marks": [28, 24, 26, 29, 30],
        "fees_paid": True
    }
]
))
# print(get_top_students(
#        [
#     {
#         "name": "Jenish",
#         "age": 22,
#         "grade": "A",
#         "marks": [30, 80, 90, 90, 20],
#         "fees_paid": True
#     },
#     {
#         "name": "Ram",
#         "age": 21,
#         "grade": "B",
#         "marks": [25, 30, 20, 15, 18],
#         "fees_paid": False
#     },
#     {
#         "name": "Sita",
#         "age": 20,
#         "grade": "A",
#         "marks": [35, 28, 32, 30, 25],
#         "fees_paid": True
#     },
#     {
#         "name": "Hari",
#         "age": 22,
#         "grade": "C",
#         "marks": [20, 15, 18, 22, 19],
#         "fees_paid": False
#     },
#     {
#         "name": "Gita",
#         "age": 21,
#         "grade": "B",
#         "marks": [28, 24, 26, 29, 30],
#         "fees_paid": True
#     }
# ]
# ))                
unpaid_student = []         
for student in students:
     if student["fees_paid"]==False:
          unpaid_student.append(student["name"])

print(unpaid_student)

while len(unpaid_student) > 0:
     student = unpaid_student.pop()
     print(student)

for subject in available_subjects:
     


