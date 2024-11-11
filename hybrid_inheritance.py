class Human:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
    def show_details(self):
        print("Name:",self.name)
        print("Age:",self.age)
class Person(Human):
    def __init__(self,name,age,address):
        Human.__init__(self,name,age)
        self.address = address 
    def show_details(self):
        Human.show_details(self)
        print("Address:",self.address)
class Program:
    def __init__(self,program_name,duration):
        self.program_name = program_name 
        self.duration = duration 
    def show_details(self):
        print("Program name:",self.program_name)
        print("Duration:",self.duration)
class Student(Person):
    def __init__(self,name,age,address,program):
        Person.__init__(self,name,age,address)
        self.program = program 
    def show_details(self):
        Person.show_details(self)
        self.program.show_details()

program = Program("Computer Science","4 Years")
student = Student("Mahruful Alam",23,"Badda,Dhaka",program)
student.show_details()
