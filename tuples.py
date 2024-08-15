tup =[1,2,4,8,75,4] #convert tuple to list then print
tup[0]=87
print(type(tup),tup)

tup=(1,2,3,4,7,8,)
tup2=("red","green","black")
print(tup)
print(tup2)

details=("Abhejeet",18,"FYBScIt",9.8)
print(details)

# count
tuple1 = (0,1,2,3,2,3,7,3,5,4,8,9)
res=tuple1.count(3)
print("count of 3 in tuple1 is",res)

# Index
tuple1 = (0,1,2,3,2,3,7,3,5,4,8,9)
res=tuple1.index(3,4,8)
print("first occourence of 3 is",res)