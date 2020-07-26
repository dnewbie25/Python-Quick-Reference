"""Write a function that does the same as the strip( ) method
The strip method removes whitespaces at the start and end of a string
"""

import re

text_to_strip = input("Enter your text here:\n")

def myOwnStrip(text):

  replace = ''

  startWhitespaceRegex = re.compile(r'^\s+') # matches starting whitespaces

  endWhitespaceRegex = re.compile(r'\s+$') # matches whitespaces at the end

  no_start_whitespace_string = startWhitespaceRegex.sub(replace, text) # replace starting whitespaces with no characters

  no_end_whitespace_string = endWhitespaceRegex.sub(replace, no_start_whitespace_string) # replace ending whitespaces with no characters

  return no_end_whitespace_string

print(myOwnStrip(text_to_strip))
