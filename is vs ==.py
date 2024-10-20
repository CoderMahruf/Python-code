# is & == is a comparigon operator 
a=[1,2,3]
b=[1,2,3]
print(a == b) #compare value
print(a is b) #compare exact location of object in memory

a="Shuvo"
b="Shuvo"
print(a == b)
print(a is b)

a=5
b=5
print(a == b)
print(a is b)

a =(1,2,3)  # tuple is immutable 
b =[1,2,3]
print(a == b)
print(a is b)

a = None
b = None
print(a == b)
print(a is None)
print(a is b)