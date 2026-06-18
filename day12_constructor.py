class Test():
    a= 10
    b = 11

    def __init__(self):
        print("I am here.")
        return 

obj = Test()

obj1 = Test()

class Math():
    # a = 10
    # b = 11

    def __init__(self,a,b):
        self.a = b
        self.b = b
        print(f'the value of a is {a}')
        print(f'the value of a is {b}')

    def add(self):
        return self.a+self.b
obj =Math(10,29)
print(obj.add())
