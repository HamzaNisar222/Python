class Animal:
    
    def alive(self):
        print("This animal is alive")
    
    def eat(self):
        print("This animal is eating")    
    def sleep(self):
        print("This animal is sleeping")
        


class Rabit(Animal):
    def run(self):
        print("This rabit runs very fast ") 


class Dod(Animal):
    def bark(self):
        print("this dog barks")
        

class Hawk(Animal):
    def fly(self):
        print("This hawk can fly")
        
                        
rabbit= Rabit()
dog=Dod()
hawk=Hawk()


rabbit.alive()
rabbit.run()

dog.eat()
dog.bark()

hawk.sleep()
hawk.fly()        
                   
    