"""
1. Hospital Staff Management System

A hospital wants to manage its staff using the following hierarchy:

Person → Employee → Doctor

Requirements:
Person stores name, age, and gender.
Employee stores employee ID and salary.
Doctor stores specialization and consultation fee.
Tasks:
Implement the multilevel inheritance hierarchy.
Create constructors for all classes.
Display complete doctor information.
Calculate monthly income using salary and consultation fees.
Create multiple doctor objects and store their data.
"""


class Person:
    name = "Jenish"
    age = 22
    gender = "Male"


class Employee(Person):
    employee_Id = 1
    salary = 100000


class Doctor(Employee):
    specialization = "Neurosurgeon"
    consulation_Fee = 2000

    def monthly_income(self):
        return self.consulation_Fee + self.salary

    def doctor_info(self):
        return f"""Doctor Info 
        Name:{self.name} 
        Age :{self.age}
        Gender: {self.gender} 
        Employee_id : {self.employee_Id} 
        Salary : {self.salary+self.consulation_Fee}"""


obj = Doctor()
print(obj.doctor_info())
