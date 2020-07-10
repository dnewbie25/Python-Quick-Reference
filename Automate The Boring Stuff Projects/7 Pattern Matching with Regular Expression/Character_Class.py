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

"""When you use a caret ^ outside a regex class it means that the match must occur at the beginning of a string"""

beginnin_match = re.compile(r'^Hello')

test_caret_beginning = beginnin_match.search('Hallo, world! Hello')

print(test_caret_beginning == None) # It's True because Hello is at the end, it won't match it so the return value is None

"""The $ sign means the regex must end with the specified string"""

end_with_Regex = re.compile(r'\d$') #The string must end with a number

test_ending_1 = end_with_Regex.search('Your number is 42 followed by three')

print(test_ending_1 == None) # returns True because the string ends with letters

test_ending_2 = end_with_Regex.search('Your number is 43')

print(test_ending_2.group()) # returns the last digit, 3

# a string that starts and end with a number

start_end_Regex = re.compile(r'^\d+$') # it means the match should start and end with a number, no matter the length of the number (that's why we put a + sign)

test_start_end = start_end_Regex.search('125412 followed by 1124') 

print(test_start_end == None) # returns True because there are letters

test_start_end_2 = start_end_Regex.search('1245424242')

print(test_start_end_2.group()) # returns the number 1245424242





