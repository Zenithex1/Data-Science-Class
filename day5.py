a = [1,2,3,4,5,6]
print(a)
print(type(a))
print(len(a))

a = ["hello",1,2.5,True,False]

print(a)
print(a[0])
print(a[-2])
# 0 is the starting index and -1 is the last index always
# index starts from -5 to 4

# print(a[9]) # index out of range

b = ["apple",54,12.3,False,"Orange",True,21]
print(b[0:5]) # it will print from 0 index to 4 index 

print(b[1:]) # will print from first index to last indexx
print(b[:4]) # will print from first index till forth index
print(a[:]) # will print the whole list

# list methods

# append(add data at the end of the list)
c = [1,2,3,4,5,6]
c.append(5)
c.append('Jenish')
print(c)

# insert(add data at a specific index)
c.insert(2,'Shrestha') # 2 is the index and the back part is what we want to add
print(c)

# extemd

a = [1,2,3,4,5,6]
b= [7,8,9,0]
a.extend(b)
print(a)
b.extend(b)
print(b)

# concat
a = [1,2,3,4,5,6]
b= [7,8,9,0]

c = a+b
a = a+b
print(c)
print(f'This is {a}')

# method to remove data from list

a = [1,2,3,4,5,6]
del a[0]
# del a it deltes the variable a not recommended
print(a)

a = [1,2,3,4,5,6,7]
data = a.pop() # remove last data from the list
print(a)
print(data)

a = [1,2,3,4,5,6,7]
data = a.pop(1) # removes index 1  and saves it to data
print(a)

# remove  - remove according to value
a = ["apple",54,3,False,"orange",True,False] # remove the first occurence
a.remove(False)

#clear - empties the list completely
a = ["apple",54,3,False,"orange",True,False] # remove the first occurence
a.clear()
print(a)

a = [1,2,3,[2,3,4]]
print(a[-1][2])
