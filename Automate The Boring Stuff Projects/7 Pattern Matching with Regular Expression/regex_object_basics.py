import re

patter_match = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # Create the regex object

match_test = patter_match.search('My number is 415-555-4242.') # Create the match object

print(f"Phone number found: {match_test.group()}") # display the matched object with the regex object pattern
#######################################################################################
print("\n\n--------------Grouping with Parenthesis-----------------\n\n")

# If you want for instance separate the are code from the rest of the phone number

area_code_match = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') # Here you have two separate groups

complete_number = area_code_match.search('My number is 415-555-4242.')

print(f"Area code is {complete_number.group(1)}, phone number is {complete_number.group(2)}")

# If you want to print all the number you put 0 or left the parenthesis empty

print(f"group(0) = {complete_number.group(0)} | group() = {complete_number.group()}")

'''If you want to call all the group you can use Multiple Assignment'''

print(complete_number.groups()) # group() is different from groups(), this last one retrieves all the groups in your program as a Tuple

# Prints ('415', '555-4242')

areaCode, mainNumber = complete_number.groups() # Assign a variable to each group

print(areaCode) # 415
print(mainNumber) # 555-4242
#######################################################################################
print("\n\n--------------Matching Parenthesis-----------------\n\n")

# If you also need to match a parenthesis just use the escape character '\'

parenthesis_match = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
parenthesis_test = parenthesis_match.search('My phone number is (415) 555-4242')

print(f"Area code: {parenthesis_test.group(1)}. Phone Number: {parenthesis_test.group(2)}") # Prints 'Area code: (415). Phone Number: 555-4242'

'''If you want to detect special characters, use a \ escape character'''

'''Special characters in RegEx: . ^ $ * + ? { } [] \ | ( )'''
#######################################################################################

print("\n\n--------------Matching Multiple Groups with | Pipe character-----------------\n\n")

'''The Pipe | character works for finding alternative patterns'''

heroes_match = re.compile(r'Batman|Tina Fey')

heroes_test1 = heroes_match.search('Batman and Tina Fey')

heroes_test2 = heroes_match.search('Tina Fey & Batman')

print(f"In test one we found: {heroes_test1.group()} & In test 2 we found: {heroes_test2.group()}")

'''We all know batman names his gadgets with 'Bat' at the beginning. We can use the | pipe to match his objects'''

bat_match = re.compile(r'Bat(man|mobile|arang|copter)') # This will match Bat... and the rest of the word it finds

batarang = bat_match.search('I lost my Batarang')
batmobile = bat_match.search('Hurry up! To our Batmobile')

print(f"In my hand I got my {batarang.group()}")
print(f"Robin let's get in our {batmobile.group()}")

# The parenthesis also works as a grouping parenthesis

print(batmobile.groups()) # Prints ('mobile',) --> a tuple of 1 item
print(batmobile.group()) # Prints 'Batmobile'
print(batmobile.group(1)) # Prints 'mobile'

#######################################################################################
print("\n\n--------------Optional Matching with ? Question Mark-----------------\n\n")
