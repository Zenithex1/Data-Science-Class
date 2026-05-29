if 1 == 1:
    print("This is a correct statement")
    print("This is also the corrrect statementt")

print("======" * 4)
a = 1
b = 2
if a > 2 and b == 2:
    print("This is a good sign.")
else:
    print("This is a bad sign")

print("======" * 4)


marks = 100
if marks > 100 or marks < 0:
    print("Wrong Input")
elif marks >= 80 and marks <= 100:
    print("Distinction")
    if marks == 80:
        print("Lucky")
    elif marks == 100:
        print("topper")
elif marks >= 60 and marks < 60:
    print("First Division")
elif marks >= 50 and marks < 60:
    print("Second Division")
else:
    print("Fail")

if 1==2: # this doesnt work since the head if is not true the nested if doesnt work
    print("ture") 
    if (2==2):
        print("not true")

gender = "M"

# singel line if 
gender = "F"
data = "Male" if gender == "M" else "Female"
print(data)

marks = 50
data = "Distinction" if data =="50" else "First Dvision"
print(data)
print("======" * 4)


stu_marks = int(input("Enter your marks: "))
att_percent = int(input("Enter your attendance percentage: "))
fam_income  = float(input("Enter your family income: "))

if stu_marks>= 85:
    if att_percent >= 90:
        if fam_income < 300000:
            print("You have gained full Scholarship")
        else:
            print("You have gained half Scholarship")
    else:
        print("Attendance too low")
else:
    print("Not eligible")

