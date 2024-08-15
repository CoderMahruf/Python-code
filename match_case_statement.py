x = int(input("enter a num:"))
match x:
    case 0:
        print("case is zero")
    case 5:
        print("case is 5")
    case _ if x != 70:
        print(" x is not 70")
    case _ if x != 60:
        print("x is not 60")
    case _:
        print(x)
    
x = 4
match x:
        case 0:
            print("case is zero")
        case 4 if x % 2 == 0:
            print("x % 2 == 0 case is 4")
        case _ if x < 10:
            print("x is < 10")
        case _:
            print(x) 