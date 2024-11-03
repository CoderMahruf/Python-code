# dir() method 
# x = [1,2,3]
x = (1,2,3)
print(dir(x))
print(x.__add__)

# __dict__ attribute
class Person:
     def __init__(self,name,age):
         self.name = name
         self.age = age
         self.version = 2
obj = Person("Shuvo",23)
print(obj.__dict__)

# help method 
print(help(str))  #The help() function is used to get help documentation for an object, including a description of its attributes and methods.
print(help(Person))