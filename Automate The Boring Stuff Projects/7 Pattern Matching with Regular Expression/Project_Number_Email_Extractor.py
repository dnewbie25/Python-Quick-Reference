import re # for regexes
import pyperclip # for copy/paste strings
"""
Check for email and phone numbers in the copy clipboard once the user uses CTRL + C

We need three basic things:
1-Get the text off the clipboard
2-Find all phones and email addresses in the copied text
3-Paste them onto the clipboard

Once you have figured out the past three basic actions, you need to split them into small problems:
1-Get the text off the cliboard
  a- Use pyperclip module to copy and paste strings
2-Find numbers and emails
  a-Create two regexes, one for phones and one for emails
  b-Find all the matches inside the clipboard for both regexes
3-Paste them
  a-Neatly format the matched text into a single string to paste
  b-Display some message if no matches were found
"""

# You can start in whatever order you want, but at the end you must join all the individual solutions for each small problem

"""Step 1 - Create the regexes for phone numbers"""

# We'll use r.VERBOSE to add comments inside the regex and ''' to separate it and make it measier to read

phoneRegex = re.compile(r'''(
  (\d{3}|\(\d{3}\))?    # are code with or without parenthesis. Optional. Remember \( \) matches parenthesis
  (\s|-|\.)?            # separator whitespace, - or . optional if there's no area code
  (\d{3})               # first 3 digits
  (\s|-|\.)             # separator, Mandatory. It can be either whitespace, - or .
  (\d{4})               # last 4 digits
  (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension, optional. Matches any number of spaces followed by ext, x or ext. followed by any number of spaces and two to 5 digits
)''', re.VERBOSE)

"""Create email regex"""

# This regex won't match every possible email, but at least it will match almost every professional email

emailRegex = re.compile(r'''(
  [a-zA-Z0-9._%+-]+   # username. Creates a class that matches 1 or more of the combinations inside [lower, upper case, numbers . % - + symbols]
  @                   # @ symbol
  [a-zA-Z0-9.-]+       # domain name with . or -
  (\.[a-zA-Z]{2,4})   # dot something

)''', re.VERBOSE)

"""Find matches in clipboard"""




"""Copy results to the clipboard"""

