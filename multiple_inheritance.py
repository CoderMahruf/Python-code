class Employee:
    def __init__(self,name):
        self.name = name 
    def show(self):
        print(f"The name is {self.name}.")
class Dancer:
    def __init__(self,dance):
        self.dance = dance 
    def show (self):
        print(f"The dance is {self.dance}.")
class EmployeeDancer(Employee,Dancer):
    def __init__(self,name,dance):
        self.name = name 
        self.dance = dance 
obj = EmployeeDancer("Shuvo","Kathak")
print(obj.name)
print(obj.dance)
obj.show()
print(EmployeeDancer.mro()) #The Method Resolution Order (MRO) is the set of rules that construct the linearization.


class Animal:
    def __init__(self,name,species):
        self.name = name 
        self.species = species 
    def make_sound(self):
        print("Sound made by the Animal.")
class Mammal:
    def __init__(self,name,fur_color):
        self.name = name 
        self.fur_color = fur_color 
class Dog(Animal,Mammal):
    def __init__(self,name,breed,fur_color):
        Animal.__init__(self,name,species = "Dog")
        Mammal.__init__(self,name,fur_color)
        super().make_sound()
        self.breed = breed 
    def make_sound(self):
        print("Balk!")
obj = Dog("Dog","Doggerman","Dog")
obj.make_sound()


