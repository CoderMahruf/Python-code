class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y
obj = Shape(5,6)
print(obj.area())