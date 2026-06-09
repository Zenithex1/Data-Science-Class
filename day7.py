# membership operator 
a= [1,2,40,20,10,2,12,12,2]
print(10 in a)
print(200 in a)

# for loop
a= [1,2,40,20,10,2,12,12,2]
for i in a :
    print(i)

for data in "hello":
    print(data)

world_cup_data = {
    "tournament": "FIFA World Cup",
    "year": 2022,
    "host_country": "Qatar",
    "winner": "Argentina",
    "runner_up": "France",
    "golden_boot": "Kylian Mbappe",
    "golden_ball": "Lionel Messi",
    "total_teams": 32,
    "total_matches": 64,
    "total_goals": 172
}
for j in world_cup_data:
    print(j)

print("************"*3)

for j in world_cup_data:
    print(world_cup_data[j])
print("************"*3)

for j in world_cup_data.values():
    print(j)
print("**********")
for k,j in world_cup_data.items():
    print(k,j)
a = [1,2,4,5,6,7,10,12,15,17,19]
for i in a:
    if i % 2 == 0:
        print(f'It is even')
    else:
        print(f'it is odd')
#break
a = [1,2,4,5,6,7,10,12,15,17,19]
for i in a:
    if i == 2:
        break # the code stops here

a = [1,2,4,5,6,7,10,12,15,17,19]
#continue
for i in a:
    if i == 2:
        continue # the code skips if there is 2 here
    
  

# range

a= 1
for i in range(1,11):
    print(f'{a} X {i} = {a*i}')

for i in range(1,11):
    print(f'2 X {i} = {i*2}')
print("***********"* 3)
mixed_list = [1, 2.5, "apple", 4, 5.5, "banana", 7, 8.8, "cat", 10]

for i in mixed_list:
    if type(i) == float: # wrong approach
        print(i)

print("***********"* 3)

for i in mixed_list:
    if isinstance(i,float):
     print(i)

for i in [1,2,3]:
    for j in [2,3,4,5]:
        print(i,j)

print("**********")
a= [1,2,3,4,5,6]
print(sum(a))
print("**********")

s = 0
for i in a:
        s = s + i  
print(s)