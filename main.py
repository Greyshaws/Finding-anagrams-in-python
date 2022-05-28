# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(s1, s2):
    # [assignment] Add your code here

    if (sorted(s1)== sorted(s2)):
        print ("True")
    else:
        print ("False")

    return True

s1 = input("Type in your first word \n")
s2 = input("Type in your second word \n")

find_anagrams(s1, s2)