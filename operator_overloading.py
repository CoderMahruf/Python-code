class Point:
    def __init__(self,x,y):
        self.x = x 
        self.y = y 
    def __add__(self,other):
        return Point(self.x + other.x,self.y + other.y)
    def __str__(self):
        return f"{self.x}x + {self.y}y"
obj1 = Point(7,8)
print(obj1)
obj2 = Point(5,6)
print(obj2)

print(obj1 + obj2)
print(type(obj1 + obj2))

class Vector:
    def __init__(self,i,j,k):
        self.i = i 
        self.j = j
        self.k = k 
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    def __add__(self,x):
        # return f"{self.i+x.i}I + {self.j+x.j}J + {self.k+x.k}K"    #type of string
        return Vector(self.i + x.i,self.j + x.j,self.k + x.k)       #type of Vector
obj1 = Vector(3,5,6)
print(obj1)
obj2 = Vector(1,2,3)
print(obj2)

print(obj1 + obj2)
print(type(obj1+obj2))