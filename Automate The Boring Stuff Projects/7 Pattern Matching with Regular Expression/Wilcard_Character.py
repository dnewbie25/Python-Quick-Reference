import re

"""The wildcard is . a dot
it means any character except a newline"""

atRegex = re.compile(r'.at')

test = atRegex.findall('The cat in the hat sat on the flat mat 5at.')

print(test) # prints ['cat', 'hat', 'sat', 'lat', 'mat', '5at']

"""Matching everything with dot-star .* """

# remember the dot means any character and the * means zero or more characters

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')

test2 = nameRegex.search('First Name: Al Last Name: Smith')

print(test2.group(1)) # Prints 'Al'

print(test2.group(2)) # Prints 'Smith'

print(test2.group()) # Prints 'First Name: Al Last Name: Smith'

print(test2.groups()) # returns a tuple ('Al', 'Smith')

"""The above is a greedy expression, if you can to match just the regex use a non-greedy expression"""

## Greedy

greedyRegex = re.compile(r'<.*>')
greedy_test = greedyRegex.search('<To serve man> for dinner >')

print(greedy_test.group()) # prints <To serve man> for dinner > , it means it will print everything until it finds the last > sign

## Non Greedy

nongreedyRegex = re.compile(r'<.*?>')
nongreedy_test = nongreedyRegex.search('<To serve man> for dinner >')

print(nongreedy_test.group()) # prints <To serve man>, ends once it finds the first >


"""Mtaching New Lines with the dot character """

# use re.DOTALL to match everything, INCLUDING New Lines

match_newLineRegex = re.compile(r'.*', re.DOTALL)

newLine_test = match_newLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law').group() # you can either put the group() here or inside the print()

print(newLine_test)

# Prints 

# Serve the public trust.
# Protect the innocent.
# Uphold the law

# Without DOTALL it would print 'Serve the public trust.'


