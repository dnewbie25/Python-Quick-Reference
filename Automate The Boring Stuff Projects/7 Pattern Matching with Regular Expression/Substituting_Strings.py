import re

"""
You can substitute strings using sub( ) in RegEx
"""

# RegEx can be used to replace text, not only to find it

# The first argument is the RegEx to match and the second one the text you want to add instead

namesRegex = re.compile(r'Agent \w+')

text_to_replace = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob')

print(text_to_replace) # Prints 'CENSORED gave the secret documents to CENSORED'

"""You can also match groups and replace it"""

names_groupRegex = re.compile(r'Agent (\w)\w*')

test_groups = names_groupRegex.sub(r'\1*****','Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')

print(test_groups) # Prints 'A***** told C***** that E***** knew B***** was a double agent.'

