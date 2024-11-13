# time.time()
import time
print(time.time())

# time.sleep()
import time
print("Start:", time.time())
time.sleep(2)
print("End:", time.time())

print(4)
time.sleep(3)
print("This is printed after 3 seconds")

# time.strftime()
import time
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(formatted_time)