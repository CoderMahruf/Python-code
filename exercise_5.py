string=input("Enter a messge:")
words=string.split(" ")
coding=input("1 for Coding or 0 for Decoding:")
coding=True if (coding=="1") else False
print(coding)
# Coding
if (coding):
    newords=[]
    for word in words:
        if(len(word)>=3):
            r1="dsf"
            r2="jkr"
            stringnew=r1 + word[1:] + word[0] + r2
            newords.append(stringnew)
        else:
            newords.append(word[::-1])
    print(" ".join(newords))
# Decoding
else:
    newords=[]
    for word in words:
        if(len(word)>=3):
            stringnew=word[3:-3]
            stringnew=stringnew[-1]+ stringnew[:-1]
            newords.append(stringnew)
        else:
            newords.append(word[::-1])
    print(" ".join(newords))
    
    