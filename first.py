print("Hey",7,8,sep="!",end="47\n")
print("shuvo")

list1 = [7,8,7,[-8,7],["apple","banana"]]
print(list1)

tuple1 = (("parrot","sparrow"),("Lion","Tiger"))
print(tuple1)

dict1 = {"name":"Shuvo","age":22,"canVote":True}
print(dict1)

# typecasting
string = "87"
num = 52
var1= string_as_num = int(string)
sum = string_as_num + num
print("The sum of both the num :",sum)


x = input("Enter a name:")
print("My name is",x)
a = input("Enter a first num:")
b = input("Enter a second num:")
print(a+b)
print(int(a)+int(b))


import calendar
yy = 2024
dd = 7
print(calendar.month(yy,dd))

import time
timestamp = time.strftime("%H:%M:%S")
print(timestamp)

for i in range(10):
    print("7 X",i+1,"=",7*(i+1))

num = int(input("Enter a number:"))
if (num % 2) == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")