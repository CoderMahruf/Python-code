# Inheritane in Python  
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