# car.py
class Car:
    
    def __init__(self, name, make, model, year):
        self.name = name
        self.make = make
        self.model = model
        self.year = year
    
    def start(self):
        print("This car is running")
    
    def stop(self):
        print("This car has stopped")

# Instantiate the Car class and call its methods
car1 = Car("Ford", "Mustang", "GT", 2024)
car1.start()
