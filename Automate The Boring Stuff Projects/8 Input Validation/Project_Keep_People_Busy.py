import sys
import pyinputplus as pyip 



def keepBusyHours():
  response = pyip.inputYesNo("Do you want to know how to keep an idio busy for hourse?\n", caseSensitive=False, yesVal='yes')

  if response == 'no':
    
    return "Thanks for playing. Have a nice day"
  else:
    
    keepBusyHours()

keepBusyHours()
    



