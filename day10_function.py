def add():
    a = 10
    b = 20
    c = a+b
    print(c)

def adds():
    a = 10
    b = 20
    c = a+b
    return c,b,a # during multiple return value it returns in tuple since it is ordered it is not done in set because set is unordered

add()
result =adds()
print(result)

def subtract(a,b):
    c = a-b
    return c

result = subtract(5,4)
print(subtract(65,34))
print(result)

def sum_of_list(a):
    if isinstance(a,list):
        sum = 0
        for i in a:
            sum = sum + i
        return sum
    else:
        return "Wrong data type provide data in list"

print(sum_of_list([1,2,3,4,5]))
print(sum_of_list([1,2]))
print(sum_of_list(1))