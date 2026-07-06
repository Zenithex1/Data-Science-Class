f = open('day1.py','r')
print(f.read())

f = open('day9.py','r')
print(f.read())


f = open('day17.py','w') # write mode remove all the data and rewrite from scartch
f.write("Write mode \n")
f.close()

f = open('day17.py','a')
f.write("append mod\n")
f.close()

# context manager
with open('day17.py','a') as f:
    f.write(f'This is written from context manager')

import csv
# with open('data.csv','r') as f:
#     reader = csv.reader(f)
#     for i in reader:
#         print(i[1])

data = [['4',"Jen","hre",'98']]
with open('data.csv','a',newline = '') as file:
    writer = csv.writer(file)
    writer.writerows(data)