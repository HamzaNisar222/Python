class Organinsm:
    alive=True

class Animal(Organinsm):
    def __init__(self,name):
        self.name=name
    
    def eat(self):
        print("This "+ self.name +" is eating")
    def sleep(self):
        print("this animal is sleeping")    

class Dog(Animal):
    def bark(self):
        print("This dog is barking")        
        
        
dog=Dog("dog")

print(dog.alive)
dog.eat() 
dog.sleep()      