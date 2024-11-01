class ExampleClass:
    @classmethod
    def factory_method(cls, argument1, argument2):
        return cls(argument1, argument2)
# Example     
class Employee:
    company = "Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")
    @classmethod
    def changecompany(cls,newCompany):
        cls.company = newCompany
        
obj = Employee()
obj.name = "Shuvo"
obj.show()
obj.changecompany("Tesla")
obj.show()
print(Employee.company)

