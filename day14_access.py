class Person():
    __game = "PS5"
    test = __game

    def __display(self):
        return self.test
    
obj = Person()
#print(obj.__game)
print(obj.test)
#print(obj.__display())


print("===================================="*2)

# 🚗 Vehicle Tracking System (Design)
# 🧱 Class: Vehicle (Base Class)

# Attributes:

# vehicle_id → public (can be accessed anywhere)
# _speed → protected (used inside class + subclasses)
# __engine_code → private (hidden, not directly accessible in child classes)

# Methods:

# __init__(vehicle_id, speed, engine_code)
# get_speed() → returns current speed
# set_speed(speed) → updates speed (with validation if needed)
# get_engine_code() → safe method to access private engine code
# display_vehicle_info() → prints basic vehicle details
# 🧱 Class: Car (inherits Vehicle)

# Attributes:

# inherits:
# vehicle_id
# _speed
# cannot directly access:
# __engine_code (private)

# Additional Attributes:

# car_type (e.g., SUV, Sedan)

# Methods:

# __init__(vehicle_id, speed, engine_code, car_type)
# accelerate(increment) → increases speed using _speed
# brake(decrement) → decreases speed safely
# show_car_info() → displays car-specific + vehicle info
# get_engine_info() → calls parent method (not direct access)
# 🧱 Class: ElectricCar (inherits Car)

# Attributes:

# inherits all from Car and Vehicle
# battery_level

# Methods:

# __init__(vehicle_id, speed, engine_code, car_type, battery_level)
# charge(amount) → increases battery level
# use_battery(amount) → decreases battery level
# show_electric_status() → shows speed + battery info
# accelerate_fast() → overrides accelerate (optional behavior using battery impact)
# 🔐 Key Access Behavior (Important Concept Task)

# In this system:

# vehicle_id → accessible in all classes
# _speed → accessible in Car and ElectricCar
# __engine_code → ONLY accessible inside Vehicle via methods

class Vehicle():
    vehicle_id= 101
    speed = 50
    __engine_code = "N1N"

    def get_speed(self):
        return f'Current Speed: {self.speed}'
    
    def set_speed(self,speed):
        self.speed = speed
        return f'Updated speed: {self.speed}'
    
    def get_engine_code(self):
        return f'Engine code: {self.__engine_code}'
    
    def display_vehicle_info(self):
        return(f'vehicle_id:{self.vehicle_id}\n'
               f'vehicle_speed:{self.speed}\n'
               f'vehicle_engine_code:{self.get_engine_code()}\n'
               f'vehicle_speed:{self.speed}\n')

class Car(Vehicle):
    car_type = "SUV"

    def accelerate(self,increment):
        self.speed += increment
        return f'After accelerate:{self.speed}'

    def brake(self,decrement):
        self.speedd -= decrement
        return f'After breaking:{self.speed}'
    
    def show_car_info(self):
        return (f'Vehicle Info:{self.display_vehicle_info()}\n'
                f'Car_type = {self.car_type}')
    
    def get_engine_info(self):
        return f'EngineInfo = {self.get_engine_code}'
    
class ElectricCar(Car):
    battery_level = 30
    def charge(self,amount):
        self.battery_level += amount
        return self.battery_level

    def use_battery(self,amount):
        self.battery_level -= amount
        return self.battery_level

    def show_electric_status(self):
        return (f'Speed: {self.get_speed()}\n'
                f'Battery Info: {self.battery_level}\n'
                f'Battery after charge :{self.charge(20)}\n'
                f'Battery after using: {self.use_battery(10)}')
    
    def mapping(self,):
        self.data = {
            "10":10,
            "20":20,
            "30":30,
            "40":40,
            "50":50,
            "60":60
        }   
        return f'{self.data.get(self.battery_level,15)}'
    def accelerate_fast(self, increment):
        self.speed += increment * 2
        self.battery_level -= 5
        return f"Speed: {self.speed}, Battery: {self.battery_level}"

obj = ElectricCar()
print(obj.show_electric_status())