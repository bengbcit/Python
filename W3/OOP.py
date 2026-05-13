# Create an inheritance hierarchy
# 1. Create a Vehicle base class (attributes: name, speed)
# 2. Create subclasses: Car, Bike, Truck
# 3. Each subclass has its own speak method (e.g., sound)
# 4. Create a list, iterate through all vehicles and output

# submission code should:
# - have clear inheritance relationships
# - have method overriding
# - demonstrate polymorphism

class Vehicle:
    # This is the base class for all vehicles
    def __init__(self,name,speed):
        self.name = name
        self.speed = speed
    # The speak method will be overridden by subclasses to provide specific sounds for each vehicle type    
    def speak(self):
        return f"{self.name} makes a sound"
    # The info method provides basic information about the vehicle, which can also be overridden by subclasses for more specific details
    def info(self):
        return f"{self.name} (speed: {self.speed} km/h)"
    
# The Car, Bike, and Truck classes inherit from the Vehicle class and override the speak and info methods to provide specific behavior for each type of vehicle    
class Car(Vehicle):
    def speak(self):
        return f"{self.name} says: Vroom!"
    def info(self):
        return f"{self.name} (Car, speed: {self.speed} km/h)"

class Bike(Vehicle):
    def speak(self):
        return f"{self.name} says: Ring ring!"
    def info(self):
        return f"{self.name} (Bike, speed: {self.speed} km/h)"

class Truck(Vehicle):
    def speak(self):
        return f"{self.name} says: Honk honk!"
    def info(self):
        return f"{self.name} (Truck, speed: {self.speed} km/h)"
'''
Here we create a list of different vehicle instances and demonstrate polymorphism by calling the speak and info methods on each vehicle, 
which will execute the overridden methods specific to each vehicle type
'''

vehicles = [Car("Tesla", 120), Bike("Giant", 20), Truck("Volvo", 80)]

# We loop through each vehicle in the list and print the output of the speak and info methods, 
# showcasing how each vehicle type has its own implementation of these methods
for vehicle in vehicles:
    print(vehicle.speak())
    print(vehicle.info())
