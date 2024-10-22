# using decoretor functions to greet 
def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for using this functions")
    return mfx
@greet
def hello():
    print("Hello World") 
# greet(hello)()
hello()


# practicl use case 
def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for the using this functions")
    return mfx
@greet
def hello():
    print("Hello World")
    
def add(a,b):
    print(a+b)

hello()
