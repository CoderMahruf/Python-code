# seek functions 
with open('file.txt','r')as f:
    f.seek(10)
    data=f.read(5)
    print(data)
  
    
# tell position
with open('file.txt','r')as f:
    f.seek(10)
    print(f.tell())

# truncate function 
with open('sample.txt','w')as f:
    f.write('Hello World')
    f.truncate(5)