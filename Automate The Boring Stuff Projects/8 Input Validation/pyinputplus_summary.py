"""
pyinputplus offers a number of ways to validate data, the most common functions will be:
inputStr() --> strings

inputNum() --> int or float numbers based on if the number has a decimal point or not 

inputChoice() --> select from provided choices

inputMenu() --> provides a menu with numbers or letters

inputDatetime() --> enter date and time

inputYesNo() --> enter yes or no

inputBool() --> enter True or False and returns a boolean value

inputEmail() --> enter email

inputFilepath() --> ensures user enter a valid path and filename, can check if the file exists

inputPassword() --> replace characters with * to hide passwords
"""

# let's import with an alias in order to not having to tyype pyinputplus all the time

import pyinputplus as pyip

response = pyip.inputNum(prompt="Enter a number: ") # here you can put prompt= or just add the input instruction string
print("Correct")
"""
If the user enters an invalid values such as special characters or letters it will prompt 'x is not a number'
"""

##### How to specify a numerical range for the input
print("---------------   min, max, greaterThan, lessThan arguments  -------------------------")
################### min, max, greaterThan, lessThan   ##################

"""You only need to put a second argument specifying the range"""

# let's create an input of positive numbers starting from 4 and less than 11

positiveValues = pyip.inputNum("Enter a positive number: ", min=4, lessThan=11)
print("Correct")

print("---------------   blank keyword argument    -------------------------------")

blankInput = pyip.inputNum("Enter a number or a blank (hit Enter): ", blank=True) # By enabling blank you can type enter or a whitespace and it will accept that input. Otherwise it will prompt 'Blank values are not allowed.'
print("Correct")


print("---------------   limit, timeout and default arguments    -------------------------------")

# when you want to specify a limit number of attempts to enter the data or a limit time to enter it you can use these arguments

timerInput = pyip.inputYesNo("The reactor will nlow up. Do you want to stop the Uranium enrichment?: ", timeout=3, blank=True) # 3 seconds. If the user does not enter anything within 3 seconds a TimeoutException error will raise

limitInput = pyip.inputNum("You have 3 attempts to enter the number I'm thinking of: ", limit=3) # 3 attempts

defaultInput = pyip.inputNum("Enter a number or let the program enter my favorite number: ", limit=2, default=10) # enters 10 if the user does not enter any number

print(defaultInput) # prints 10 or the number entered by the user