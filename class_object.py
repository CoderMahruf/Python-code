class Person:
    name = "Shuvo"
    occupation = "Software Developer"
    networth = 10
    def info(self):   #The self parameter is a reference to the current instance of the class, and is used to 
                      # access variables that belongs to the class.
        print(f"{self.name} is a {self.occupation}")
        
a = Person()
b = Person()
c = Person()

a.name = "Mahruf"
a.occupation = "Engr"

b.name = "Ehsan"
b.occupation = "Math"
# print(a.name,a.occupation)

a.info()
b.info()
c.info()


class Details:
    name = "Shuvo"
    age = 23
    def description(self):
        print("My name is", self.name, ".I am ",self.age, "years old.")
obj=Details()
obj.description()
