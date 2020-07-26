"""Write a function that does the same as the strip( ) method
The strip method removes whitespaces at the start and end of a string
"""

import re

text_to_strip = input("Enter your text here:\n")

def myOwnStrip(text, character = ''):

  if character == '':
    replace = ''

    startWhitespaceRegex = re.compile(r'^\s+') # matches starting whitespaces

    endWhitespaceRegex = re.compile(r'\s+$') # matches whitespaces at the end

    no_start_whitespace_string = startWhitespaceRegex.sub(replace, text) # replace starting whitespaces with no characters

    no_end_whitespace_string = endWhitespaceRegex.sub(replace, no_start_whitespace_string) # replace ending whitespaces with no characters

    return no_end_whitespace_string
  else:

    replace = ''

    startWhitespaceRegex = re.compile(r'^\s+') # matches starting whitespaces

    endWhitespaceRegex = re.compile(r'\s+$') # matches whitespaces at the end

    no_start_whitespace_string = startWhitespaceRegex.sub(replace, text) # replace starting whitespaces with no characters

    no_end_whitespace_string = endWhitespaceRegex.sub(replace, no_start_whitespace_string) # replace ending whitespaces with no characters

    characterRegex = re.compile(character, re.IGNORECASE)

    string_without_character = characterRegex.sub(replace, no_end_whitespace_string) # takes the no_end_whitespace_string, which is the string without starting nor ending whitespaces and removes the specified character

    return string_without_character


print(myOwnStrip(text_to_strip, 'o'))
