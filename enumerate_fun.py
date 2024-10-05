marks = [12, 15, 54, 98, 1, 45, 41]
# index =0
# for mark in marks:
#     print(mark)
#     if (index == 3):
#         print("Shuvo is pass in this exam")
#     index +=1  

for index,mark in enumerate(marks, start=1):
    # print(mark)
    print(index,mark)
    if (index == 3):
        print("Shuvo is pass in this exam")

fruits= ['apple','banana','mango']
for index,fruit in enumerate(fruits):
    print(index,fruit)


fruits=['apple', 'banana', 'mango']
for index,fruit in enumerate(fruits, start=1):
    print(index,fruit)
    
    
fruits=['apple', 'banana', 'mango']
for index,fruit in enumerate(fruits):
    print(f'{index+1}:{fruit}')
    
    
colors=['red','green','blue']
for index,color in enumerate(colors):
    print(index,color)

    
s='hello'
for index,c in enumerate(s):
    print(index+1,c)