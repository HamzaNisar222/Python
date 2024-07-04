# Abstract classes prevents a user from creating an object of it 
# compels a user from overriding an abstract method in a child class

#An  ABSTRACT CLASS IS A CLASS WHICH HAVE SEVRAL ABSTRACT METHODSS
# A ABSTRACT METHOD IS A METHOD THAT HAVE DECLARATION BUT NO IMPLEMENTATION 

from abc import ABC ,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go():
        pass
    
    @abstractmethod
    def stop():
        pass  
    
class Motorcycle(Vehicle):
    
    def go(self):
        print("You can ride the bike")
        
    def stop(self):
        print("Apply breaks and ")
        
    def started(self):
        print("motorcycle has started")
        
class Car(Vehicle):
    def go():
        print("You can now drive the car")
    
    def stop(self):
        print("Stop and turn the switch off")
        
    def started(self):
        print("Car has started")
        
        
      
bike=Motorcycle()
bike.started()

car=Car()
car.started()