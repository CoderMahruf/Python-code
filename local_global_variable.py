x = 4 #Global Variable
print(x)
def hello():
    x = 5 #Local Variable
    print(f"The local x is {x}")
    print("Hello Shuvo!")
print(f"The global x is {x}")
hello()
print(f"The local x is {x}")


x = 10 # global variable
def my_function():
  y = 5 # local variable
  print(y)
my_function()
print(x)
# print(y)   # this will cause an error because y is a local variable and is not accessible outside of the function


# Use Global Variable 
x = 10 #global variable
def my_function():
    global x
    x = 5
    y = 5 # local variable
    print(y)
my_function()
print(x)

