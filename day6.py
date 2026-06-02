a = {
    "name":"Jenish",
    "address":"Kathmandu",
    "age": 22
}

print(type(a))
print(a)
print(len(a))

a = {
    "name":"Jenish",
    "address":"Kathmandu",
    "age": 22,
    "address": "Nepal"
}

print(a)
print(len(a))

a = {
    "name":"Jenish",
    "address":"Kathmandu",
    "age": 22,
    "temp": "Nepal"
}
print(a)
print(a.keys())
print(a.values())

print(a["temp"])
print(a["name"])
# print(a["ages"]) # error 

# update
a['address'] = 'Dang'
a["ages"]= 100 # will create a new key value pair
print(a)

a.update({
    "name":"Haru",
    "temp":"Pokhara",
    "phone":980
})
print(a)
 
a = {
    "fname":"Jenish",
    "lname":"Shrestha"
}

    

a["full_name"]= (f"{a['fname']} {a['lname']}")
print(a)
# to rmeove key value pair from dict

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
#del world_cup_data
del world_cup_data['host_country']
# only stores the value
data = world_cup_data.pop('total_goals')
print(world_cup_data)
print(data)
# removes the last item and store both key and value
data = world_cup_data.popitem()
print(world_cup_data)
print(data)

world_cup_data.clear()
print(world_cup_data)
