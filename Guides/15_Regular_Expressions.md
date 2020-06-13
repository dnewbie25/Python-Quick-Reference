# RegEx or Regular Expressions

Think you want to find a phone number in a string. The phone number has a US format, which is 3 digits, hyphen, 3 digits, hyphen and then 4 digits like *555-415-8985*. 

You can create a program to match that format, but it could be so long and it will just increase in length if you also want to matche the formats with parenthesis or extensions like *(415)-585-5212* or *415-895-5245 ext 1545*.

An example of a program to match the normal expression would be:

~~~python
def isPhoneNumber(text):
  if len(text) != 12: # US phone numbers have 12 characters, hyphens included
    return False
  for i in range(0, 3): # Loops through characters 0,1,2. Remember that range is inclusive-exclusive
    if not text[i].isdecimal(): # If the character is not a decimal returns False
      return False
      
  if text[3] != '-': # If the forth character is not a hyphen returns False
    return False
  for i in range(4, 7): # Loops from 4,5,6
    if not text[i].isdecimal():
      return False # The same as with the first 3 characters
   
   if text[7] != '-': # If the seventh character is not a hyphen
     return False
   for i in range(8, 12):
    if not text[i].isdecimal(): # If it's not a decimal number (0-9)
      return False
      
   return True # If text passes all the code conditionals then it's a US valid phone number
   
print('Is 415-555-4242 a phone number?')
print(isPhoneNumber('415-555-4242')) # True
print('Is Moshi moshi a phone number?')
print(isPhoneNumber('Moshi moshi')) # False      
~~~

Dude, that's a lot of code to match 12 characters. And now think about that people that wraps their phone numbers in parenthesis or that use dots instead of hyphens, *4112.251.2545*. It's a mess to work with that and it won't be worthy to have such a huge block of code to match all possible cases.

For this parituclar set of problems very brilliant programmers created the RegEx. These are a set of rules, common to most programming languages, to simplify the characters matching process.

What took us 17 lines of code for the US standard format can be simplified in just one line:
~~~python
\d\d\d-\d\d\d-\d\d\d\d # This is all you would need using RegEx. The \d means digits. So you would search for three digits, hyphen, three digis, hyphen and four digits

# You can simplify the RegEx code much more, take a look

\d{3}-\d{3}-\d{4} # This will search for 3 digits, hyphen, three digits, hyphen and four digits
~~~
