# Method overriding 
class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        super().__init__(radius,radius) #using super keyword for overriding
    def area (self):
        return 3.15 * super().area()     
obj = Shape(5,6)
print(obj.area())

c = Circle(5)
print(c.area())


class Shape:
    def area (self):
        print("Calculating area...")
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        print("Calculating area of a circle .....")
        super().area()     #using super keyword for overriding.
        return 3.15 * self.radius * self.radius 
obj = Circle(5)
print(obj.area())
