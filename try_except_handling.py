try:
    num=int(input("Enter the num:"))
except ValueError:
    print("Number entered is not an integer")


a=input("Enter the num:")
print(f"Multiplication table of {a} is:")

try:
    for i in range(1,11):
      print(f"{int(a)} X {i} = {int(a)*i}")
except :
    print("Invalid Input!")    
    
print ("Some important line of code")
print("End of program")

try:
    num=(int(input("Enter the num:")))
    a=[5,7,8,9]
    print(a[num])
except ValueError:
    print("Number enterd is not an integer")
except IndexError:
    print("Index Error")