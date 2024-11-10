class Employee:
    def __init__(self,name):
        self.name = name 
    def show(self):
        print(f"The name is {self.name}.")
class Dancer:
    def __init__(self,dance):
        self.dance = dance 
    def show(self):
        print(f"The dance is {self.dance}")
class EmployeeDancer(Employee,Dancer):
    def __init__(self,name,dance):
        self.name = name 
        self.dance = dance 
obj = EmployeeDancer("Shuvo","Kathak")
print(obj.name)
print(obj.dance)
obj.show()
print(EmployeeDancer.mro()) #The Method Resolution Order (MRO) is the set of rules that construct the linearization.

