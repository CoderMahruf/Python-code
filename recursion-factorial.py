def factorial(num):
    if(num==1 or num==0):
        return 1
    else:
        return num * factorial(num-1)
print("Factorial:",factorial(7))


def factorial(n):
    if (n==1 or n==0):
        return 1
    else:
        return n * factorial(n-1)
print(factorial(9))


# fibonacci sequence
def fibonacci (n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(6))