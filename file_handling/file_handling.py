# File read mode 
f = open('myfile.txt', 'r')
text = f.read()
print(text)

# File Read mode 
# f = open('myfile2.txt', 'w')
# f.write("Hello, World!")
# f.close()

# File append mode 
f = open('myfile2.txt', 'a')
f.write("Hello,World!")
f.close()

with open('myfile.txt', 'a') as f:
    f.write("Hey i am inside with")