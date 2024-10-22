class Person:
    def __init__(self,name,occupation):
        print("Hey i am a Person")
        self.name = name
        self.occupation = occupation
        
    def info(self):
        print(f"{self.name} is a {self.occupation}")
        
a = Person("Shuvo","Developer")
b = Person("Ehsan","Math")
# a.name="Mahruf"
# a.occupation="Engr"
# print(a.name)
a.info()
b.info()

# Perameterized constructor 
class Details:
    def __init__(self,animal,group):
        self.animal = animal
        self.group = group
obj = Details("Crab","Crustaceans")
print(obj.animal,"belongs to the", obj.group,"group.")

# Default constructor 
class Details:
    def __init__(self):
        print("Crab belongs to the Crustaceans group.")
obj = Details()