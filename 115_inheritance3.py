# concept of hierarchical inheritance 
class MyMath:
    def getPi(self):
        #local variable 
        pi = 22/7
        return pi 
    def getSquare(self,number):
        #local variable 
        square = number * number
        return square

class Circle(MyMath):
    #create constructor 
    def __init__(self,radius):
        super().__init__() #calling parent class 
        #create instance variable
        self.radius = radius
    def getArea(self):
        pi = super().getPi() 
        square = super().getSquare(self.radius)
        area = pi * square
        return area 

class Cylinder(MyMath):
    def __init__(self,radius,height):
        super().__init__()
        self.radius = radius
        self.height = height 
    def getSurfaceArea(self):
        pi = super().getPi()
        square = super().getSquare(self.radius)
        volume = 2 * pi * self.radius * self.height + (2 * pi * square)
        return volume
    
#create circle class object
r1 = int(input("Enter Circle radius"))

c1 = Circle(radius=r1)
area = c1.getArea()
print("Area of circle ",area)

r2 = int(input("Enter  Cylinder radius"))
h1 = int(input("Enter  Cylinder height"))

#create Cylinder class object
c2 = Cylinder(radius=r2,height=h1)
surface_area = c2.getSurfaceArea()
print("Surface Area of of Cylinder ",surface_area)

