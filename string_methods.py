# upper
str1="AbCdEfGhIj"
print(str1.upper())
# lower
str1="AbCdEfGhIj"
print(str1.lower())
# strip
str2=" Silver Spoon "
print(str2.strip())
# rstrip
str2="Hello !!!"
print(str2.rstrip("!"))
# replace
str3="Silver Spoon"
print(str3.replace("Sp","M"))
# split
str3="Silver Spoon"
print(str3.split())
# capitalize
str4="hello"
print(str4.capitalize())

str4="hello World"
print(str4.capitalize())
# center
str5="Welcome to the console!!!"
print(str5.center(120))

str5="Welcome to the console!!!"
print(str5.center(120,"*"))
# count
str6="Abracadabra"
print(str6.count("a"))
# endswith
str6="Welcome to the console !!!"
print(str6.endswith("!"))
# find
str7="He's name is Dan.He is an honest man"
print(str7.find("is"))

str7="He's name is Dan.He is an honest man"
print(str7.find("Daniel"))
# index
str8="He's name is Dan.He is an honest man"
print(str8.index("Dan"))

str8="He's name is Dan.He is an honest man"
# print(str8.index("Daniel"))

# isalnum
str9="Welcometotheconsole123"
print(str9.isalnum())
# isalpha
str9="Welcome"
print(str9.isalpha())
# islower
str1="hello world"
print(str1.islower())
# isprintable
str1="We wish you a Eid Mobarak\n" #using \n its not a printable!
print(str1.isprintable())
# isspace
str2="      "       #using space
print(str2.isspace())
str2="      "       #using tab
print(str2.isspace())
# istitle
str3="World Health Organization"
print(str3.istitle())

str3="to Kil A Mocking bird"
print(str3.istitle())
# isupper
str4="WORLD HEALTH ORGANIZATION"
print(str4.isupper())
# startswith
str4="Python is a interpreted language"
print(str4.startswith("Python"))
# swapcase
str5="Python is a Interpreted Language"
print(str5.swapcase())
# title
str5=("He's name is Dan.He is an honest man")
print(str5.title())