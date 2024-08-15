# sort()

# ascending order
colors = ["voilet","indigo","blue","green"]
colors.sort()
print(colors)

num = [4,8,7,5,4,3,2,6,7,8,9,7,4]
num.sort()
print(num)
# discending order
num = [4,8,7,5,4,3,2,6,7,8,9,7,4]
num.sort(reverse=True)
print(num)

# reverse()
colors = ["voilet","indigo","blue","green"]
colors.reverse()
print(colors)

num = [4,8,7,5,4,3,2,6,7,4,8,9,7,]
num.reverse()
print(num)

# index
colors =["violet","green","indigo","blue","green"]
print(colors.index("green"))

num = [4,8,7,5,4,3,2,6,7,4,8,9,7,]
print(num.index(7))

# count
colors = ["violet","green","indigo","blue","green"]
print(colors.count("green"))

num = [4,8,7,5,4,3,2,6,7,4,8,9,7,]
print(num.count(4))

# copy

colors = ["voilet","indigo","blue","green"]
newlist=colors.copy()
print(colors)
print(newlist)  

# append
colors = ["voilet","indigo","blue"]
colors.append("green")
print(colors)

# insert
colors = ["voilet","indigo","blue"]
colors.insert(1,"green")
print(colors)

# extend
colors = ["voilet","indigo","blue","green"]
rainbow = ["orange","yellow","red","black"]
colors.extend(rainbow)
print(colors)

# concatenating two list
colors1= ["voilet","indigo","blue","green"]
colors2 = ["orange","yellow","red","black"]
print(colors1+colors2)