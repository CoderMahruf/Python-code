from functools import lru_cache
import time 

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5

# print after 5 second
print(fx(20))
print("Done for 20")
# print after 5 second
print(fx(3))
print("Done for 3")
# print after 5 second
print(fx(5))
print("Done for 5")

print(fx(20))
print("Done for 20")
print(fx(3))
print("Done for 3")
print(fx(5))
print("Done for 5")
# print after 5 second
print(fx(50))
print("Done for 50")

from functools import lru_cache 
@lru_cache(maxsize = None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci (n-2)
print(fibonacci(20))