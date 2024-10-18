# def double (x):
#     return x*2

# use lambda funtion for make the simple code 
double = lambda x: x*2
cube = lambda a: a*a*a
avg = lambda x,y,z: (x+y+z)/3
print(double(5))
print(cube(5))
print(avg(5,6,9))


def myfunc(n):
    return lambda a: a*n
mydoubler=myfunc(2)
mytripler=myfunc(3)
print(mydoubler(11))
print(mytripler(11))


def multiply_and_print(x,y):
    return 5*6
print(f"{5}*{5}={5*6}")

multiply=lambda x,y: x*y
print(f"{5}*{3}={multiply(5,3)}")