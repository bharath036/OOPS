import math

#Here try to understand the self parameter, __,
class Circle:
    def __init__(self,radius):
        self.__radius = radius 

    def area(self):
        c = math.pi*self.__radius*self.__radius
        return print(c)
    def perimeter(self):
        d = 2*math.pi*self.__radius 
        return print(d)
    
    def both(self):
        return self.area(),self.perimeter()

  
c =Circle(4)
c.area()
c.perimeter()
c.both()

