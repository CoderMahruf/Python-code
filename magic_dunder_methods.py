# __len__ method 
class Person:
    name = "Shuvo"
    def __len__(self):
        i = 0
        for c in self.name:
            i = i+1
        return i 
obj = Person()
print(obj.name)
print(len(obj))


# __str__ method 
class Employee:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return (f"The name of the Employee is {self.name} str")
 
    
# __repr__ method 
# class Employee:
#     def __init__(self,name):
#         self.name = name
    def __repr__(self):
        return (f"Employee is {self.name} repr.")
    
    
# __call__method 
# class Employee:
#     def __init__(self,name):
#         self.name = name
    def __call__(self):
        print ("Hey i am Shuvo")