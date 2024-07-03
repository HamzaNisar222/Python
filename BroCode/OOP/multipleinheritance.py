class Prey:
    
    def __init__(self,name):
        self.name=name
        
    
    def flee(self):
        print("This " + self.name + " Flees")


class Predator:
    def __init__(self,name):
        self.name=name
        
    
    def prey(self):
        print("This " + self.name + " Preys")
        
class Rabit(Prey):
    def run():
        print("This rabit runs fast")
        
class Hawk(Predator):
    pass       

class Fish(Prey,Predator):
    pass



hawk=Hawk("hawk")
hawk.prey()

rabit=Rabit("Rabbit")
rabit.flee()

fish=Fish("Fish")
fish.flee()
fish.prey()