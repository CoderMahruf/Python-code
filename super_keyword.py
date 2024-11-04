class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
class Programmer(Employee):        
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang = lang
ehsan = Employee("Ehsan",232)
shuvo = Programmer("Shuvo",258,"Ptthon")
print(ehsan.name)
print(ehsan.id)
print(shuvo.name)
print(shuvo.id)
print(shuvo.lang)

class ParentClass():
    def parent_method(self):
        print("This is the parent class.")
class ChildClass(ParentClass):
    def child_method(self):
        print("This is the child method.")
        super().parent_method()
class_object = ChildClass()
class_object.child_method()

class ParentClass1:
    def parent_method(self):
        print("This is the parent method of ParentClass1.")
class ParentClass2:
    def parent_method(self):
        print("This is the parent method of ParentClass2.")
class ChildClass(ParentClass1,ParentClass2):
    def child_method(self):
        print("This is the child method.")
        super().parent_method()
class_object = ChildClass()
class_object.child_method()

