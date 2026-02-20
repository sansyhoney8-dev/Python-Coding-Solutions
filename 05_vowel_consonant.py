# find vowel and consonant characters

character = str(input("Enter your single character:")).lower()
l1 = ["a","e","i","o","u"]
if(character in l1):
    print(f"{character} is a vowel")
else:
    print(f"{character} is a consonant ")

# WAP to check it ia vowel,number or a consonant

character = str(input("Enter your single character:")).lower()
l1 = ["a","e","i","o","u"]
if(character in l1):
    print("it is a vowel")
elif(character .isdigit()):
    print("it is a number not,not a letter")
else:
    print("it is a consonant")

