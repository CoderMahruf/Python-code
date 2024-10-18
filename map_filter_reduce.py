# map
def cube(x):
    return x*x*x
l=[1,5,6,8,11,15,18]
# newl=[]
# for item in l:
#     newl.append(cube(item))
newl=list(map(cube,l))
print(newl)

# Double each number using the map functin 
numbers=[1,2,3,4,5]
doubled=list(map(lambda x: x*2,numbers))
print(doubled)