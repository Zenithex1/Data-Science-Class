# in class
# variable = attributes
# function = methods

# always class name in capital fist letter

class Fifa():
    host_year = 2026
    host_country = "USA"

obj = Fifa()
obj.host_country = "Nepal"
obj.winner = "Argentina"
print(obj.host_country)
print(obj)
print(obj.winner)
print("--------------------"*2)
obj1 = Fifa()
print(obj1)
print(obj1.host_country)
# print(obj1.winner)# error because there is no winner attribute
print("================================"*3)

class Fifa():
    host_year = 2026
    host_country = "USA"
    match_1 = "Mexico"
    match_2 = "South Africa"
    def opening_game(self):
        return f'{self.match_1} vs {self.match_2}'    
    def today_match(self):
        print("from method",self.opening_game())
        return "Brazil vs USA"
obj = Fifa()
print("from object",obj.opening_game())
print(obj.today_match())
# print(obj1.winner)# error because there is no winner attribute













