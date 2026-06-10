#tuple

a =(1,2,3,4,5)
b = (2,3,4,5,2)
print(b.count(2))
print(b.index(4))
c =a+b
d = a*3
e = (2,3,4)
f,g,h = e
print(f"This is {f}")
for i in a:
    print(i)
print(d)
print(c)
print(type(a))
print(a[4])
#a[3]= 3 cant change because it is immutable
a = set() # empty set
print(a)



# set

a = {"Ram","Hari","Test",1,1,1,1,22,2,2}
a.add(3)
a.update([5,6])
a.remove(1)
a.discard(5)

print(a)
print(type(a))

