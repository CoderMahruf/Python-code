word = input("Enter a word: ")
coding = input("1 for Coding or 0 for Decoding:")
coding = True if (coding=="1") else False 
print(coding)
if(coding):
 #Coding
  if len(word) >=3:
    remove = word[0]
    word = word[1:]
    append = "abd"
    word = append + word + remove + "ap"
    print(word)
# Decoding
else:
  if len(word) <=3:
    remove = word[3:-3]
    remove = word[-1] + word[:-1]
    print(remove)