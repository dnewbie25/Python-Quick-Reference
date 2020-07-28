"""
pyinputplus offers a number of ways to validate data, the most common functions will be:
inputStr() --> strings

inputNum() --> int or float numbers based on if the number has a decimal point or not 

inputChoice() --> select from provided choices

inputMenu() --> provides a menu with numbers or letters

inputDatetime() --> enter date and time

inputYesNo() --> enter yes or no, y or n. It's not case sensitive

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

timerInput = pyip.inputYesNo("The reactor will nlow up. Do you want to stop the Uranium enrichment?: ", timeout=10, blank=True) # 3 seconds. If the user does not enter anything within 3 seconds a TimeoutException error will raise

limitInput = pyip.inputNum("You have 3 attempts to enter the number I'm thinking of: ", limit=3) # 3 attempts

defaultInput = pyip.inputNum("Enter a number or let the program enter my favorite number: ", limit=2, default=10) # enters 10 if the user does not enter any number

print(defaultInput) # prints 10 or the number entered by the user

print("---------------   allowRegexes and blockRegexes arguments   -------------------------------")

"""
These two keywords allow you to define a regex to determine whether the input is valid or not. You can define what's the expected input
"""

allowed_regex = pyip.inputNum("Enter a Roman Number: ",allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero']) # allows roman numbers or 'zero'
print(allowed_regex)

denied_regex = pyip.inputNum("Enter a decimal number: ", blockRegexes=[r'(I|V|X|L|C|D|M)+', r'zero']) # restricts roman numbers and 'zero' word.
print(denied_regex)


# You can specify regexes to allow and regexes to block. Below the statement allows 'caterpillar' and 'category' but blocks every toher string that starts with 'cat'
override_regexes = pyip.inputStr("Enter a word starting with 'cat': ",allowRegexes=[r'caterpillar', 'category'], blockRegexes=[r'cat'])
print(override_regexes)

print("---------------   parsing custom input with inputCustom( )   -------------------------")

"""With this function you can create your own validations, like adding numbers that adds up to 10 or even numbers only"""

# inputCustom( ) to create a function that sums the digits of the number so they add up to 10

def addsUpToTen(numbers):

  numbersList = list(numbers) # creates a list separating each character, for example 234 --> ['2', '3', '4']

  for i, digit in enumerate(numbersList): # It creates an enumerate object, which is the count number (in this case 0 unless we specify another) and the item in the list
     
    numbersList[i] = int(digit) # takes the index in the 2-tuple and use that to converte the element in the list to an integer

  '''
  Explanation of the above: An enumerate will create something like this (0, '2'), (1, '3'), (2, '4')
  with this code we make sure that every digit (the second element in the tuple which we call by using the index) will be converted to integer
  '''

  if sum(numbersList) != 10: # if the sum of the elements in the array is different from 10 raises an exception
    raise Exception(f'The digits must add up to 10, not {sum(numbersList)}')

  return int(numbers)

test_custom_input = pyip.inputCustom(addsUpToTen) # the exception created before makes that inputCustom() runs until a valid input gets entered

print(test_custom_input)