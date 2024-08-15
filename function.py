def calculateGmean(a,b):
 mean= (a*b)/(a+b)
 print(mean)
c  = 9
d = 6
if ( c > d):
    print("First num is greater")
else:
    print("Second num is greater")
x = 10
y = 55
if (x < y):
    print("first num is greater")
else:
    print("first num is less than second num ")
a = 9
b = 8
calculateGmean(a,b)
calculateGmean(x,y)
# gmean=(a*b)/(a+b)
# print(gmean)

calculateGmean(c,d)
# gmean = (c*d)/(c+d)
# print(d)





# find the number of 3 which number the largest number?
def findlargest(num1,num2,num3,num4):
    if (num1 > num2) and (num1 > num3) and (num1 > num4):
        largest = num1
    elif (num2 > num1) and (num2 > num3) and (num2 > num4):
        largest = num2
    elif (num3 > num1) and (num3 > num2) and (num3 > num4):
        largest = num3
    else:
        largest = num4
        return largest
    
num1=(int(input("Enter the num1:")))
num2=(int(input("Enter the num2:")))
num3=(int(input("Enter the num3:")))
num4=(int(input("Enter the num4:")))

largest = findlargest(num1,num2,num3,num4)
print("The largest number is among the 4 number:",largest)

 