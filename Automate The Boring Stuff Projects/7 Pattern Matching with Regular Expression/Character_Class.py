import re

"""
\d -- digits
\D -- non digits
\w -- letters, numerical digits or underscore
\W -- non letter, non numercial digit, non underscore
\s -- whitespace
\S -- non whitespace
"""

xmasRegex = re.compile(r'\d+\s\w+')
# the above means match any number of digits from 1 to infinite, followed by a whitespace, followed by any combination of characters

test = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')

print(test)


"""You can make your own class by using square brackets [ ] """

# Let's say you want a class to match vowels in lower and upper case

vowelRegex = re.compile(r'[aeiouAEIOU]') # This will match any character within that range of letters

test_vowel_class = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')

print(test_vowel_class) # returns a list with all the vowels found ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']

"""You can match anything that is not a specific character with a caret ^ 
The caret character is also known as a negative character, it matches everything except the characters you defined in the class"""

# Let's say you want to match just the consonants only, you would use ^ character

consonantRegex = re.compile(r'[^aeiouAEIOU]') # this will match anything that's not a vowel

test_consonant_class = consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')

print(test_consonant_class) # returns a list of consonants ['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']





