# Public Access Modifier in Python 
# by default accessible from outside 
class Emplyee:
    def __init__(self):
        self.name = "Shuvo"  #public variable
obj = Emplyee()
print(obj.name)

class Student:
    def __init__(self,age,name):
        self.age = age         #public variable
        self.name = name       #public variable
obj = Student(23,"Shuvo")
print(obj.age)
print(obj.name)

# Private Access Modifier in python 
class Employee:
    def __init__(self):
        self.__name = "Shuvo"
obj = Employee()
# print(obj.__dir__())   #see the all method in program using __dir__() method.
# print(obj.__name)
print(obj._Employee__name)

# Name Mangling 
class MyClass:
    def __init__(self):
        self._nonmangled_attribute = "I am a nonmangled attribute"
        self.__mangled_attribute = "I am a mangled attribute"
my_object = MyClass()
print(my_object._nonmangled_attribute)
# print(my_object.__mangled_attribute) 
print(my_object._MyClass__mangled_attribute) 

# Prodected Access modifier in python 
class Student:
    def __init__(self):
        self._name = "Shuvo"
    def _funName(self):       #protected method 
        return "Mahruful Alam"
class Subject(Student):      #inherited class
    pass
obj = Student()
obj1 = Subject()
# calling by object of Student class 
print(obj._name)
print(obj._funName())
# calling by object of Subject class 
print(obj1._name)
print(obj1._funName())