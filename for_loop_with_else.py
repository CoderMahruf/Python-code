
# for loop

for i in range(5):
    print(i)
else:
    print("Sorry no i")

for i in range(5):
    print(i)
    if i==3:
        break
else:
    print("Sorry no i")

#  while loop   
i =0
while i < 7:
    print(i)
    i=i+1
    if i == 4:
        break
else:
    print("Sorry no i ")
    
    
for x in range(5):
    print("iteratrion no {} in for loop".format(x+1))
else:
    print("else block in loop")
print("out of loop")