# # while

# i = 0
# while (i<=20):
#     if i == 2:
#      continue
#     print(i)
#     i +=1

# # random 

import random

for i in range(1,10):
   print(random.random())
print("--------------------"*2)
a = [1,22,33,"jenish"]

for i in range(1,10):
   print(random.choice(a))
print("--------------------"*2)
for i in range(1,20):
   print(random.randint(1,20))
   