class Vehicle:
    def start(self):
        print("The vehicle is staring")

class Car(Vehicle):
    def start(self):
        print("The car is staring with a key")

class Bike(Vehicle):
    def start(self):
        print("The Bike is staring with a self start button")

# create object 

c = Car()
b = Bike()

# call the overriden methods

print()
c.start()
print()
b.start()
