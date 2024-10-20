# map
def cube(x):
    return x*x*x
l=[1,5,6,8,11,15,18]
# newl=[]
# for item in l:
#     newl.append(cube(item))
newl=list(map(cube,l))
print(newl)

l=[1,3,5,7,9,11]
newl=list(map(lambda x: x*x*x,l))
print(newl)

# Double each number using the map functin 
numbers=[1,2,3,4,5]
doubled=list(map(lambda x: x*2,numbers))
print(doubled)

# filter 
l=[1,3,5,7,9,11]
def filter_function(x):
    return x>5
newl2=list(filter(filter_function,l))
print(newl2)

numbers=[1,2,3,4,5,7,8,9,10]
evens=list(filter(lambda x: x % 2 == 0 ,numbers))
print(evens)

# reduce 
from functools import reduce
l=[1,3,5,7,9]
def mysum(x,y):
    return x+y
sum=reduce(mysum,l)
print(sum)

from functools import reduce
l=[1,3,5,7,9]
sum=reduce(lambda x,y: x+y,l)
print(sum)