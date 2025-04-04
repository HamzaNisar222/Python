class Rectangle:
    def __init__(self ,length, width):
        self.length=length
        self.width=width
    
class Square(Rectangle):
    
    def __init__(self,length,width):
        super().__init__(length,width)
        
    def area(self):
        return self.length * self.width
    
class Cube(Rectangle):
    
    def __init__(self,length,width,height):
        super().__init__(length,width) 
        self.height=height
    
    def area(self):
        return self.length * self.width * self.height
    
 
square=Square(2,8)
print(square.area())

cube=Cube(2,9,7)
print(cube.area())   
                 