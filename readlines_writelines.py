f = open('myfile3.txt','r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)