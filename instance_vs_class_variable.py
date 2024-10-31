class Employee:
    companyName = "Apple"
    noofEmployee = 0
    def __init__(self,name):
        self.name = name
        self.raise_amount = 0.02
        Employee.noofEmployee  += 1
    def showdetails(self):
        print(f"The name of the Employee is {self.name} and the raise amount in {self.noofEmployee} sized  {self.companyName} is {self.raise_amount}")
        
obj1 = Employee("Shuvo")
# Employee.showdetails(obj)
obj1.raise_amount = 0.03
obj1.companyName = "Apple Bangladesh"
obj1.showdetails()

Employee.companyName = "google"
print(Employee.companyName)

obj2 = Employee("Mahruf")
obj2.companyName = "Nestle"
obj2.showdetails()

# Class Variable 
class MyClass:
    class_variable = 0
    def __init__(self):
        MyClass.class_variable += 1
    def print_class_variable(self):
        print(MyClass.class_variable)
obj1 = MyClass()
obj2 = MyClass()
obj1.print_class_variable()
obj2.print_class_variable()

#  Instance Variable 
class MyClass:
    def __init__(self,name):
        self.name = name
    def print_name(self):
        print(self.name)
obj1 = MyClass("Shuvo")
obj2 = MyClass("Mahruf")

obj1.print_name()
obj2.print_name()