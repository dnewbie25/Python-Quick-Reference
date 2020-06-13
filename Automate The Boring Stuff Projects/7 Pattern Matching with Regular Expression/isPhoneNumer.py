import re

def isPhoneNumber(text):
  if len(text) != 12: # Check if the phone number has 12 digits (US numbers)
    return False
  for i in range(0, 3):
    if not text[i].isdecimal(): # Checks if the first 3 digits are decimal numbers (only decimal numbers 0-9)
      return False
  if text[3] != '-': # the forth character must be a hyphen, if not returns False, because US numbers are in this format 999-999-9999 
    return False
  for i in range(4, 7): # Repeat the bove with the following digits
    if not text[i].isdecimal():
      return False
  if text[7] != '-':
    return False

  for i in range(8, 12):
    if not text[i].isdecimal():
      return False
  return True

''' 
print('Is 415-555-4242 a phone number?')
print(isPhoneNumber('415-555-4242')) # True
print('Is Moshi moshi a phone number?')
print(isPhoneNumber('Moshi moshi')) # False
'''

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

for i in range(len(message)):
  chunk = message[i:i+12] # Takes the characters from i to i+12...twelve characters in total
  if isPhoneNumber(chunk): # If the chunk is actually a Phone number, it returns the following
    print("Phone number found: " + chunk)

print('Done')

'''
The above piece of code does this:
* 'Call me at 4'
*	 'all me at 41'
*	 'll me at 415'
*	 'l me at 415-'

It iterates and compares 12 characters until it finds a set of 12 characters that matches the US phone number format...a tedious task that could be simplified with RegEx
'''

