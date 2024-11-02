class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    @classmethod
    def fromStr(cls,string):
        # name,salary = string.split("-")
        # return cls(name,int(salary))
        return cls(string.split("-")[0],int(string.split("-")[1]))
obj1 = Employee("Shuvo",12000)
print(obj1.name)
print(obj1.salary)

string = "John-12000"
obj2 = Employee.fromStr(string)
print(obj2.name)
print(obj2.salary)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @classmethod
    def from_string(cls,string):
        name,age = string.split(",")
        return cls (name,int(age))
person = Person.from_string("Shuvo ,23")
print(person.name,person.age)

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    @classmethod
    def squre (cls,size):
        return cls (size,size)
rectangle = Rectangle.squre(10)
print(rectangle.width,rectangle.height)