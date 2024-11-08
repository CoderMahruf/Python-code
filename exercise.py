import time
timestamp= time.strftime("%H:%M:%S")
hour = int(time.strftime("%H"))
if (hour>=0 and hour<10):
    print("good morning shuvo")
elif (hour>=10 and hour<14):
    print("Shuvo this is launch time")
elif (hour>=14 and hour<17):
    print("Hello shuvo afternoon")
elif (hour>=17 and hour<22):
    print("shuvo its now dinner time")
else:
    print("good night shuvo")
