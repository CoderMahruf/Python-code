# Inheritane in Python  
class Vehicle:
    def start(self):
        print("Vehicle is starting")
class Bike(Vehicle):
    def start(self):
        print("Bike is starting")
obj = Bike()
obj.start()


class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f"The name of Employee: {self.name} id is {self.id}")
class Programmer(Employee):
    def showlanguage(self):
        print("The Default language is Python") 
e = Employee ("Mahrurul Alam ",400)
e.showDetails()
e2 = Programmer ("Manjarul Alam ",401)
e2.showDetails()
e2.showlanguage()

# Single Inheritance 
class Parent:
    def func1(self):
        print("This function is in parent class.")
class Child(Parent):
    def func2(self):
        print("This function is in child class.")
obj = Child()
obj.func1()
obj.func2()

# Multiple Inheritance 
class Father:
    fathername = ""
    def father(self):
        print(self.fathername)
class Mother:
    mothername = ""
    def mother(self):
        print(self.mothername)
class son(Father,Mother):
    def parents(self):
        print("Mother name is: ", self.mothername)
        print("Father name is: ", self.fathername)
s1 = son()
s1.fathername = "Yousuf"
s1.mothername = "Rowson"
s1.parents()

# Multilevel Inheritance 
class Grandfather:
    def __init__(self,grandfather):
        self.grandfather = grandfather
class Father(Grandfather):
    def __init__(self,father,grandfather):
        self.father = father
        Grandfather.__init__(self,grandfather)
class Son(Father):
    def __init__(self,son,father,grandfather):
        self.son = son
        Father.__init__(self,father,grandfather)
    def print_name(self):
        print("Grandfather name is:",self.grandfather)
        print("Father name is:",self.father)
        print("Son name is:",self.son)
obj = Son("Shuvo","Yousuf","Bashar")
obj.print_name()

# Hiererchical Inheritance 
class Parent:
    def func1(self):
        print("This function is in parent class.")
class Child1(Parent):
    def func2(self):
        print("This function is in Child 1.")
class Child2(Parent):
    def func3(self):
        print("This function is in Child 2.")
obj1 = Child1()
obj2 = Child2()
obj1.func1()
obj1.func2()
obj2.func1()
obj2.func3()

# Hybrid Inheritance 
class School:
    def func1(self):
        print("This function is in School")
class Student1(School):
    def func2(self):
        print("This function is in student1")
class Student2(School):
    def func3(self):
        print("This function is in student2")
class Student3(Student1,School):
    def func4(self):
        print("This function is in student 3")
obj1 = Student2()
obj1.func3()
obj = Student3()
obj.func1()