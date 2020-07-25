"""
This project will take text from the clipboard, split it into phone numbers and emails and then paste them neatly formatted.
It will use the pyerclip and regex modules
"""

import re, pyperclip

"""For this project I need
-Get the text off the clipboard
-Search for phones and email 
-Paste them neatly formatted
"""

# Get the text off the clipboard

clipboard_text = str(pyperclip.paste()) # this one stores everything copied in the clipboard_text variable

# Search for phones and email. By using ''' you will be able to add commens to the regex

phonesRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))? # matches 123 or (123) area code. Optional
(\s|-|\.)? # whitespace, dash or dot. Optional
(\d{3}|\(\d{3}\)) # 3 digits. Mandatory
(\s|-|\.) # whitespace, dash or dot. Mandatory
(\d{4}) # 4  digits, no parenthesis
(\s*(ext|e|ext.)\s*(\d{2,5}))? # matches 0 or more * whitespaces before the extension number, which is 2-5 digits long
)''', re.VERBOSE) # allows comments by using '''

emailRegex = re.compile(r'''(
[a-zA-Z0-9-+.*/%_]+ # email addres
@ # @
[a-zA-Z0-9-._+/%]+ # domain
(\.[a-zA-Z]{2,4}) # . something
(\.[a-zA-Z]{2,4})? #. something. Optional, like udea.edu.co
)''', re.VERBOSE)

# paste neatly formatted

# first you put the data in a list
matches = []

for groups in phonesRegex.findall(clipboard_text):
  phone_number = '-'.join([groups[1], groups[3], groups[5]])
  if groups[6] != '':
    phone_number += ' extension ' + groups[8]
  
  matches.append(phone_number)

for groups in emailRegex.findall(clipboard_text):
  matches.append(groups[0])

# then you paste it in the console

if len(matches) > 0:
  pyperclip.copy('\n'.join(matches))
  print("Copied to clipboard:")
  print('\n'.join(matches))
else:
  print("No phone numbers or email addresses found.")








