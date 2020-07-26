"""Function to test a strong password. It must have at least:
8 characters long
Contains upper and lower case characters
1 digit minimum
"""

import re

password_to_test = input("Enter a password to test: ")

def regexStrong(password):

  lowercaseRegex = re.compile(r'[a-z]') # any lower case letter

  uppercaseRegex = re.compile(r'[A-Z]') # any upper case letter

  digitsRegex = re.compile(r'[0-9]') # any digit

  lowercase_count = lowercaseRegex.findall(password)

  uppercase_count = uppercaseRegex.findall(password)

  digits_count = digitsRegex.findall(password)

  total_length = (lowercase_count + uppercase_count + digits_count) # joins the three tuples
  

  if len(total_length)<8: # 8 characters long
    return "Your password is too short. Use 8 or more characters"
  elif len(lowercase_count) < 1: # at least 1 lower case
    return "Your password need digits, upper and lower case characters"
  elif len(uppercase_count) < 1: # at least 1 upper case
    return "Your password need digits, upper and lower case characters"
  elif len(digits_count) < 1: # at least 1 digit
    return "Your password need digits, upper and lower case characters"
  else:
    return "Your password is Super Strong"

print(f"Password to test: {password_to_test}\n{regexStrong(password_to_test)}")
  