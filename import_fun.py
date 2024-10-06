# import pandas
# pandas.read_csv()

import math
math.floor(4.2343)

result=math.sqrt(9)
print(result)

# from keyword 
from math import sqrt
result=sqrt(9)
print(result)

from math import sqrt,pi
result=sqrt(9)
print(result)
print(pi)

from math import sqrt,pi
result=sqrt(9) *pi
print(result)

from math import *
result=sqrt(9)
print(result)
print(pi)
print(e)

# "as" keyword
# from math import pi,sqrt as s 
import math as m
result=m.sqrt(9)* m.pi
print(result) 

import math as math_builtin_python
result=math_builtin_python.sqrt(9)* m.pi
print(result) 

# dir function 
# Python has a built-in function called dir that you can use to view the names of all the functions and variables defined in a module.
import math
print(dir(math))
print(math.nan, type(math.nan))


# from shuvo import welcome,shuvo
# from shuvo import *
import shuvo as s
s.welcome()
print(s.shuvo)