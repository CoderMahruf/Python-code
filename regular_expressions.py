# Searching for a pattern in re using re.search() Method
import re 
pattern = "army"
text = '''Donkey Kong Country is a 1994 platform game developed by Rare and published by Nintendo for the Super Nintendo Entertainment System. It follows the gorilla Donkey Kong and his nephew Diddy Kong as they set out to recover their stolen banana hoard from the crocodile King K. Rool and his army, the Kremlings. Nintendo commissioned Rare to revive the dormant Donkey Kong franchise as it sought a game to compete with Sega's Aladdin (1993).'''
match = re.search(pattern,text)
print(match)

import re 
pattern = r"expression"    # Define a regular expression pattern
text = "Hello World"      # Match the pattern against a string
match = re.search(pattern,text)
if match:
    print("Match Found")
else:
    print("Match Not Found")

# Searching for a pattern in re using re.findall() Method
import re
pattern = r"expression"
text = "The cat is in the hat."
matches = re.findall(pattern, text)
print(matches)

# Replacing Pattern 
import re
pattern = r"[a-z]+at"
text = "The cat is in the hat."
matches = re.findall(pattern, text)
print(matches)
new_text = re.sub(pattern, "dog", text)
print(new_text)

# Extracting information from a string
import re
text = "The email address is mahruf9060@gmail.com."
pattern = r"\w+@\w+\.\w+"
match = re.search(pattern, text)
if match:
    email = match.group()
    print(email)
