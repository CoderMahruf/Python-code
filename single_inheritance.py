class Animal:
    def __init__(self,name,species):
        self.name = name 
        self.species = species 
    def make_sound(self):
        print("Sound made by the Animal.")
class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species = "Dog")
        self.breed = breed
    def make_sound(self):
        print("Bark!")
d = Dog("Dog","Doggerman")
d.make_sound()

c = Animal("Dog","Dog")
c.make_sound()

# Quick Quiz: Implement a Cat class by using the animal class. Add some methods specific to cat.
# Base class
class Animal:
    def __init__(self, species):
        self.species = species
    def eat(self):
        print(f"The {self.species} is eating.")
    def sleep(self):
        print(f"The {self.species} is sleeping.")

# Derived Cat class
class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__("Cat")
        self.name = name
        self.breed = breed
    def purr(self):
        print(f"{self.name} the {self.breed} is purring.")
    def scratch(self):
        print(f"{self.name} the {self.breed} is scratching.")
    def meow(self):
        print(f"{self.name} the {self.breed} says 'Meow!'")
        
# Test the Cat class
my_cat = Cat("Elsa", "Siamese")
my_cat.eat()
my_cat.sleep()
my_cat.purr()
my_cat.scratch()
my_cat.meow()
