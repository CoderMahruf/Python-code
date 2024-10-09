import os

folders=os.listdir("data")
print(os.getcwd()) # find the directory file name
# os.chdir("/users") # Change the file directory name
# print(os.getcwd()) 


for folder in folders:
    print(os.listdir(f"data/{folder}"))
    print(folder)