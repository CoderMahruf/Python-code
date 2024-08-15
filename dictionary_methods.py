# update()
ep1={611:79,612:85,613:90,614:77}
ep2={711:89,712:86}
ep1.update(ep2)
print(ep1)

info={'name':'karan','age':19,'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2002})
print(info)

# clear()
info={'name':'karan','age':19,'eligible':True}
info.clear()
print(info)

# pop()
info={'name':'karan','age':19,'eligible':True}
info.pop('age')
print(info)

# popitem()
info={'name':'karan','age':19,'eligible':True,'DOB':2002}
info.popitem()
print(info)

# del()
info={'name':'karan','age':19,'eligible':True,'DOB':2002}
del info['DOB']
print(info)


info={'name':'karan','age':19,'eligible':True,'DOB':2002}
del info
print(info) # throw the error