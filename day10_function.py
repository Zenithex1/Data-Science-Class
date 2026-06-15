def add():
    a = 10
    b = 20
    c = a + b
    print(c)


def adds():
    a = 10
    b = 20
    c = a + b
    return (
        c,
        b,
        a,
    )  # during multiple return value it returns in tuple since it is ordered it is not done in set because set is unordered


add()
result = adds()
print(result)


def subtract(a: int, b: int):
    c = a - b
    return c


result = subtract(5, 4)
print(subtract(65, 34))
print(result)


def sum_of_list(a):
    if isinstance(a, list):
        sum = 0
        for i in a:
            sum = sum + i
        return sum
    else:
        return "Wrong data type provide data in list"


print(sum_of_list([1, 2, 3, 4, 5]))
print(sum_of_list([1, 2]))
print(sum_of_list(1))


# # default arguments
# def sum(a=0, b=0):
#     return a + b


# print(sum(2, 4))


def employee(name: str, age):
    print(name, age)


# keyword arguments
employee("Jenish", 12)
employee(12, "Jenish")

employee(age=12, name="Jenish")


def user_info(fname, lname):
    return f"my name is {fname} {lname}"


print(user_info(lname="Shrestha", fname="Jenish"))
print("============================")


# default argument
def area(r, pie=3.14):
    return pie * r**2


print(
    area(7, 5)
)  # if i write 5 here it will take 5 but if not written anything it takes the defalut value given in  parameter
print(area(7))
print("================" * 3)

#* args
def marks(*data):
    print(type(data))
    print(data)
    print('\n')

marks(1,2,3,4,5)
marks(2,3,4)
marks()
print("==========="*2)

def avg(*args):
    if len(args) == 0:
        print("please send any data")
    total =0
    for i in args:
        total = (total+i)

    return total/len(args)

print(avg(2,2))
print("==========="*2)

def test(*args):
    print(args[0])
    print(args[2])


test(10, 20, 30, 400)
print("===================" * 2)
square = lambda x: x * x
print(square(5))

add = lambda a, b: a + b
print(add(5, 6))


def add(a):
    a = 0
    c = a
    return c


print(add(2))


def outer():
    """
    Returns the squre of x
    """
    msg = "Hello"

    def inner():
        print(msg)

    inner()


outer()


#
def order_food(item, quantity, price):
    price = quantity * price
    if price >= 1000:
        price = price - (price * 10) / 100
    else:
        price = price - (price * 5) / 100
    return f"The {item} bought in {quantity} quanity with total price after discount {price}"


print(order_food("Laptop", 10, 100))
print(order_food("Laptop", 10, 9))

a =(1,2,3,4)
print(len(a))

# keyword arguments

def user_info(**data):
    print(data)
    print(type(data))

user_info(name="jenish",age=22)

def test(a,*args,**kwargs):
    print(a)
    print(args)
    print(kwargs)

test(1,2,3,4,5,name = "Jenish")
print("============"*3)
# def calculate_salary(base_salary, *bonuses, **deductions):
    
#     for i in bonuses:
#         base_salary = base_salary + i
#     for i,j in deductions.items():
#         if isinstance(j, int):
#                 base_salary = base_salary - j
#         else:
#                 print( f"Wrong data type in deduction only integer")
#                 break
#     print(base_salary)

def calculate_salary(base_salary,*bonuses,**deductions):
    if(len(bonuses)==0 and len(deductions)==0):
        return base_salary
    total_bonus = sum(bonuses)
    if len(deductions)==0:
        return base_salary + total_bonus
    deductions_values = deductions.values()
    deductions_total = 0
    for i in deductions_values:
        if not isinstance(i,int):
            continue
        deductions_total = deductions_total + i
    return base_salary+ total_bonus - deductions_total
    




print(calculate_salary(50000))

print(calculate_salary(50000, 2000))

print(calculate_salary(
    50000,
    2000,
    3000,
    tax=5000
))
print(calculate_salary(
    50000,
    2000,
    3000,
    tax=5000,
    insurance=1200,
    extra = "sudan"
))

# list comprehension
a =[2,3,4,5,6]
