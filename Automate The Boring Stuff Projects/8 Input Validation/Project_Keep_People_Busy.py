import sys
import pyinputplus as pyip 

# Method one
"""
def keepBusyHours():
  response = pyip.inputYesNo("Do you want to know how to keep an idio busy for hourse?\n", caseSensitive=False, yesVal='yes')

  if response == 'no':
    
    return "Thanks for playing. Have a nice day"
  else:
    
    keepBusyHours()

keepBusyHours()
""" 

# Method two

while True:
  question = "Do you want to know how to keep in idiot busy?\n"
  response = pyip.inputYesNo(question)

  if response == 'yes':
    continue
  elif response == 'no':
    print("Thank you for playing. Have a great day!")
    break


