num = int(input("Enter a number:"))
if (num < 0):
    print("Number is negetive.")
elif (num > 0):
    if (num < 10):
        print("The number is between 1-10")
    elif (num > 10 and num < 20):
        print("The number is between 10-20")
    else:
        print("Number is greater then 20")
else:
    print("Number is zero")    