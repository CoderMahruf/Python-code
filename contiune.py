for i in range (12):
    if (i == 10):
        print ("Skip the itration")
        continue
    print("5 X",i,"=",5*i)
    
for i in [2,3,4,6,8,0]:
    if (i % 2 != 0):
        continue
    print(i)
      