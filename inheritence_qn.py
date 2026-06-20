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
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Employee(Person):

    def __init__(self, name, age, gender, employeeId, salary):
        self.employeeId = employeeId
        self.salary = salary
        super().__init__(name, age, gender)


class Doctor(Employee):
    def __init__(
        self, name, age, gender, employeId, salary, specialization, consulationFee
    ):
        self.consulationFee = consulationFee
        self.specialization = specialization

        super().__init__(name, age, gender, employeId, salary)

    def doctor_info(self):
        return f"""Doctor Info
        Name:{self.name}
        Age :{self.age}
        Gender: {self.gender}
        Employee_id : {self.employeeId}
        Salary : {self.salary+self.consulationFee}"""


obj = Doctor("jenish", 22, "Male", 1, 100000, "Neurosurgeon", 5000)
print(obj.doctor_info())

print("=======================" * 3)
# 2. University Student Record System

# Hierarchy:

# Person → Student → GraduateStudent

# Requirements:
# Person: name, address, contact number.
# Student: roll number, department, GPA.
# GraduateStudent: thesis title, research area.
# Tasks:
# Create the class hierarchy.
# Accept details from the user.
# Display complete student information.
# Check whether the student qualifies for a research scholarship.
# Demonstrate access to members inherited from all levels.


# class Person:
#     def __init__(self):
#         self.name = input("Whats your name: ")
#         self.address = input("Whats your address: ")
#         self.contact_number = input("Whats your contact number: ")


# class Student(Person):
#     def __init__(self):
#         super().__init__()
#         self.roll_number = input("Whats your roll number: ")
#         self.department = input("Whats your department: ")
#         self.GPA = float(input("Whats your GPA: "))


# class GraduateStudent(Student):
#     def __init__(self):
#         super().__init__()
#         self.thesis_title = input("Whats your thesis title : ")
#         self.research_area = input("Whats your research area: ")

#     def scholarshipinfo(self):
#         if self.GPA > 3.5:
#             return f"Scholarship achieved "
#         else:
#             return f"No scholarship "

#     def displayInfo(self):
#         return (
#         f"\n===== Student Record System =====\n"
#         f"Name            : {self.name}\n"
#         f"Address         : {self.address}\n"
#         f"Contact         : {self.contact_number}\n"
#         f"Roll No         : {self.roll_number}\n"
#         f"Department      : {self.department}\n"
#         f"GPA             : {self.GPA}\n"
#         f"Thesis Title    : {self.thesis_title}\n"
#         f"Research Area   : {self.research_area}\n"
#         f"Scholarship     : {self.scholarshipinfo()}\n"
#     )



# obj = GraduateStudent()
# print(obj.displayInfo())

# print("=========================*3")

# 3. Vehicle Rental Company

# Hierarchy:

# Vehicle → Car → LuxuryCar

# Requirements:
# Vehicle: vehicle number, brand, base rental rate.
# Car: seating capacity, fuel type.
# LuxuryCar: chauffeur charge, luxury tax.
# Tasks:
# Create constructors for all classes.
# Calculate total rental cost for a given number of days.
# Print all vehicle details.
# Show how LuxuryCar can use data inherited from both parent classes.
# class Vehicle():
#     def __init__(self,vehicle_number,brand,base_rental_rate):
#         self.vehicle_number = vehicle_number
#         self.brand = brand
#         self.base_rental_rate = base_rental_rate
    

# class Car(Vehicle):
#     def __init__(self,vehicle_number,brand,base_rental_rate,seating_capacity,fuel_type):
#         self.seating_capacity = seating_capacity
#         self.fuel_type = fuel_type
#         super().__init__(vehicle_number,brand,base_rental_rate)

# class LuxuryCar(Car):
#     def __init__(self,vehicle_number,brand,base_rental_rate,seating_capacity,fuel_type,chauffeur_charge,luxury_tax):
#         self.chauffeur_charge = chauffeur_charge
#         self.luxury_tax = luxury_tax
#         super().__init__(vehicle_number,brand,base_rental_rate,seating_capacity,fuel_type)

#     def rental_cost(self,days):
#         total_rental_cost = self.base_rental_rate * days + self.luxury_tax
#         return total_rental_cost
#     def vehicle_detail(self):
#         return f"""
#         Vehicle Details:
#         ----------------
#         Vehicle Number   : {self.vehicle_number}
#         Brand            : {self.brand}
#         Base Rate        : {self.base_rental_rate}
#         Seating Capacity : {self.seating_capacity}
#         Fuel Type        : {self.fuel_type}
#         Chauffeur Charge : {self.chauffeur_charge}
#         Luxury Tax       : {self.luxury_tax}
#         total_rent_cost : {self.rental_cost(10)}
#         """ 
# obj = LuxuryCar("BA 12 PA 1234", "Toyota", 5000, 4, "Petrol", 1000, 500)
# print(obj.vehicle_detail())
# 4. Banking System

# Hierarchy:

# Account → SavingsAccount → PremiumSavingsAccount

# Requirements:
# Account: account number, holder name, balance.
# SavingsAccount: interest rate.
# PremiumSavingsAccount: reward points and cashback percentage.
# Tasks:
# Implement deposit and withdrawal operations.
# Calculate annual interest.
# Calculate cashback earned from transactions.
# Display complete account information.
# 5. Employee Promotion System

class Account():
    def __init__(self,accountNumber,holderName,balance):
        self.accountNumber = accountNumber
        self.holderName = holderName
        self.balance = balance

        def deposit(self,amount):
            self.amount = amount
            if self.amount>0:
                self.balance =+ self.amount
            else:
                return 'Cannot deposit less than 0'
            
        def withdraw(self):
            if self.amount > 0:
                self.balance =-self.amount
            else:
                return 'Cannot withdraw less than 0'

        def AccountInfo(self):
            return( f'Account Number : {self.accountNumber}\n'
            f'Holder Name: {self.holderName}\n'
            f'Balance: {self.Balance}\n'
            )
            

class SavingsAccount(Account):
    def __init__(self, accountNumber, holderName, balance,interestRate):
        super().__init__(accountNumber, holderName, balance)
        self.interestRate = interestRate

    def interest(self,interest):
        self.interest = interest
        self.interest = (self.interestRate * self.balance)   /100

    def displaySavingsInfo(self):
           self.AccountInfo()
           return f'Intrest Rate : {self.interest(10)}'
    
class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, accountNumber, holderName, balance, interestRate,rewardPoints,cashbackRate):
        super().__init__(accountNumber, holderName, balance, interestRate)
        self.rewardPoints = rewardPoints
        self.cashbackRate = cashbackRate

    def cashBack(self):
        self.cashBack = (self.amount * self.cashbackRate)/ 100
        self.balance += self.cashBack
        return self.balance



# Hierarchy:

# Employee → TeamLead → ProjectManager

# Requirements:
# Employee: employee ID, name, basic salary.
# TeamLead: team size, leadership bonus.
# ProjectManager: project budget, management allowance.
# Tasks:
# Create constructors using multilevel inheritance.
# Calculate total monthly salary.
# Display complete employee information.
# Create at least three project manager records.
# 6. E-Commerce Seller Platform

# Hierarchy:

# User → Seller → VerifiedSeller

# Requirements:
# User: username, email.
# Seller: store name, total sales.
# VerifiedSeller: verification badge status, commission discount.
# Tasks:
# Implement the hierarchy.
# Calculate seller earnings after commission deduction.
# Display complete seller information.
# Determine whether a seller qualifies for verification.
# 7. Smart Home System

# Hierarchy:

# Device → SecurityDevice → SmartCamera

# Requirements:
# Device: device ID, power status.
# SecurityDevice: alarm status.
# SmartCamera: storage capacity, recording hours.
# Tasks:
# Create constructors for all classes.
# Calculate remaining storage.
# Display full device details.
# Demonstrate use of inherited attributes.
# 8. Ride Sharing Application

# Hierarchy:

# Person → Driver → PremiumDriver

# Requirements:
# Person: name, phone number.
# Driver: vehicle number, completed rides.
# PremiumDriver: loyalty points, premium membership fee.
# Tasks:
# Calculate monthly earnings.
# Calculate loyalty rewards.
# Display complete driver profile.
# Update completed ride statistics.
# 9. Company Asset Tracking System

# Hierarchy:

# Asset → ElectronicAsset → Laptop

# Requirements:
# Asset: asset ID, purchase date.
# ElectronicAsset: warranty period, power rating.
# Laptop: RAM size, storage capacity.
# Tasks:
# Display complete laptop details.
# Determine whether warranty is active.
# Calculate depreciation value after a given number of years.
# Store and manage multiple laptops.
# 10. Airline Membership Program

# Hierarchy:

# Passenger → FrequentFlyer → GoldMember

# Requirements:
# Passenger: passenger ID, name.
# FrequentFlyer: total miles traveled.
# GoldMember: bonus points and lounge visits.
# Tasks:
# Calculate reward points based on miles.
# Track lounge access usage.
# Display complete member information.
# Determine eligibility for special benefits.
