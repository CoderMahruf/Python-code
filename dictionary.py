dic={
    "Shuvo": "Human being",
    "Spoon": "Object"
}
print(dic["Shuvo"])

dic={
    987:"Shuvo",
    554:"Ehsan",
    254:"Sabbir",
    654:"Masum"
}
print(dic[554])

# Accessing single value
info={'name':'karan','age':19,'eligible':True}
print(info['name'])
print(info.get('eligible2'))  #wrong key use to this method,but it not throw error

# Accessig multiple values
info={'name':'karan','age':19,'eligible':True}
print(info.values())


# Accessing key
info={'name':'karan','age':19,'eligible':True}
print(info.keys())

for key in info.keys():
    # print(info[key])
    print(f"The value corresponding to key {key} is:{info[key]}.")

# Accsessing key value pairs
info={'name':'karan','age':19,'eligible':True}
print(info.items())
    
    
info={'name':'karan','age':19,'eligible':True}
for key,value in info.items():
    print(f"The corresponding to the key {key} is: {value}.")