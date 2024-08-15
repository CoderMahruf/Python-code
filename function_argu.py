def average(a,b):
    print("Average is",(a+b)/2)
average(5,6)
# default argument
def average(a = 6,b = 9):
    print("Average is ",(a+b)/2)
average(5,)

def name(fname,mname="jhon",lname="alisa"):
    print("Hello,",fname,mname,lname)
name("Amy","Shuvo","rick")
# keyword argument
def average(b = 6,a = 9):
    print("Average is ",(a+b)/2)
average()

def name(fname,mname,lname):
    print("Hello,",fname,mname,lname)
name(mname="shubh",lname="ritu",fname="sihab")

# required arguments

def average(a,b = 9):
    print("Average is ",(a+b)/2)
average(a = 5,)

# def name(fname,mname,lname):
#     print("Hello,",fname,mname,lname)
# name("amy","shaoun")


def name(fname,mname,lname):
    print("Hello,",fname,mname,lname)
name("amy","shaoun","shima")

# variable length argument
# arbitary argument
def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Avarage is",sum/len(numbers))
average(5,6,7,1)

def name(*name):
    print("Hello",name[0],name[1],name[2])
name("Hridoy","Habu","Kabila")

# keyword arbitary argument
def name(**name):
    print("Hello,",name["fname"],name["mname"],name["lname"])
name(fname="riaz",mname="rahman",lname="mou")

# return statement
def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return sum/len(numbers)
c = average(5,6,7,1)
print(c)

def name(fname,mname,lname):
    return "Hello, "+fname+" "+mname+" "+lname
print(name("James","Hames","Rodriguiz"))