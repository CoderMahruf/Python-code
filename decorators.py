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
    def mfx(*args,**kwargs):
        print("Good Morning")
        fx(*args,**kwargs)
        print("Thanks for the using this functions")
    return mfx
@greet
def add(a,b):
    print(a+b)
# greet(add)(5,3)
add(5,3)

'''In this example, the log_function_call decorator takes a function as an argument and returns a new function that logs the function call before and after the original function is called.'''

import logging
def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b