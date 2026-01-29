#Write a Python app that has the following classes:
#A super class called Vehicle, 
#   which contains an attribute for 
#       vehicle type, such as car, truck, plane, boat, or a broomstick.
#A class called Automobile 
#   which will inherit the attributes from Vehicle 
#       and also contain the following attributes:
#       year
#       make
#       model
#       doors (2 or 4)
#       roof (solid or sun roof).
#Write an app that will accept user input for a car. The app will store car into the vehicle type in your Vehicle super class. 
#The app will then ask the user for the year, make, model, doors, and type of roof and store thdata in the attributes above.
#The app will then output the data in an easy-to-read and understandable format, such as this:
#   Vehicle type: car
#   Year: 2022
#   Make: Toyota
#   Model: Corolla
#   Number of doors: 4
#   Type of roof: sun roof

class Vehicle:
    def __init__(self, vehicle_type: str) -> None:
        self.vehicle_type: str = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type: str, year: int, make: str, model: str, doors: int, roof: str) -> None:
        super().__init__(vehicle_type)
        self.year: int = year
        self.make: str = make
        self.model: str = model
        if doors == 2 or doors == 4:
            self.doors: int = doors         #(2 or 4)
        else:
            raise ValueError("Door must be 2 or 4")
        if rood.lower() == 'solid' or roof.lower() == 'sun roof':
            self.roof: str = roof.lower()       #(solid or sun roof).
        else:
            raise ValueError('roof must be "solid" or "sun roof"')
    
    def __init__(self):
        return (f"Vehicle type: {self.vehicle_type}\n")
    
year = int = int(input())
make = input()
model = input()
doors = int = int(input())
roof = input()
car = Automobile('car', year, make, model, doors, roof)
print(car.vehicle_type, car.year, car.make, car.model, car.doors, car.roof)
print(car)