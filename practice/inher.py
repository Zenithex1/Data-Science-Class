class Animal():
    def speak(self):
        print("Some sound")

class Dog(Animal):
    pass
obj = Dog()
obj.speak()

class Person():
    def introduce(self):
        print("I am a person")

class Student(Person):
    pass
obj = Student()
obj.introduce()

class Vehicle:
    def __init__(self,brand):
        self.brand = brand

class Car(Vehicle):
    pass
obj = Car("toyota")
print(obj.brand)

class Data:
    def load(self):
        print("loading data")

class CleanData(Data):
    def clean(self):
        print("Cleaning data")

obj = CleanData()
obj.load()
obj.clean()

class Logger:
    def log(self):
        print("Logging info")

class Saver:
    def save(self):
        print("Saving data")

class Pipeline(Logger,Saver):
    pass

obj = Pipeline()
obj.save()
obj.log()

# 1. Basic Multilevel Inheritance

# Create three classes:

# A with method a()
# B inherits A and adds method b()
# C inherits B and adds method c()

# 👉 Create an object of C and call all methods.
class A():
    def a(self):
        print("This is the first level")

class B(A):
    def b(self):
        print("this is the second level")

class C(B):
    def c(self):
        print("This is the third level")

obj = C()
obj.a()
obj.b()
obj.c()

# 2. Method Access Check

# Given:

# Class Animal has method eat()
# Class Dog inherits Animal
# Class Puppy inherits Dog

# 👉 What methods can an object of Puppy access?

class Animal():
    def eat(self):
        print(f'It is eating')

class Dog(Animal):
    pass

class Puppy(Dog):
    pass

obj = Puppy()
obj.eat()

# 3. Multiple Inheritance Basics

# Create:

# Class Logger with method log()
# Class Saver with method save()
# Class System inherits both

# 👉 Create object and call both methods.
class Logger():
    def log(self):
        print(f'It is logged in')

class Saver():
    def save(self):
        print(f'It is saved')

class System(Logger,Saver):
    pass

obj = System()
obj.log()
obj.save()