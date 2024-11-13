a = True 
print(a := False)

numbers = [1,2,3,4,5]
while (n := len(numbers)) >0:
    print(numbers.pop())

names = ["Shuvo","Mehedi","Sifat"]
if (name := input("Enter the name: "))in names:
    print(f"Hello, {name}!")
else:
    print("Name not Found.")

# not using warlus operator 
foods = list()
while True:
    food = input("What food do you like? ")
    if food == "quit":
        break 
    foods.append(food)

# using warlus operator 
foods = list()
while (food := input("What food do you like? ")) != "quit":
    foods.append(food)