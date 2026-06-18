class Parent():
    a = 10
    b = 100

    def add(self):
        return self.a + self.b
    
    def out(self):
        return self.a%2
class Child(Parent):
    a = 123
    c = 1012 

class GrandChild(Child):
    a =  13

    def display(self):
        return self.b-self.c
    


obj = Child()
print(obj.c)
print(obj.b)
print(obj.a)
print(obj.add())
print(obj.out())
obj = GrandChild()
print(obj.display())

print("==================="*3)
class Parent():
    a = 10
    b = 11

class Parent1():
    c = "this is c"
    d = "this is d"

class Child(Parent,Parent1):
    b = 20
print(Child.__mro__) # method resolution order it checks which class to check first

obj = Child()
print(obj.d)
print("==================="*3)

class Parent():
    def __init__(self):
        print("I am from parent")

class Child(Parent):
    def __init__(self):
        print("I am from child")
        super().__init__()

obj = Child()
