
'''Reading Files'''

### This first one reads all the file

with open('Files Samples/pi_digits.txt') as file_objetc:
  content = file_objetc.read()
print(content.rstrip())

print("\n\n----------Reading Line By Line-----------------\n\n")

with open('Files Samples/pi_digits.txt') as filename:
  line_number = 1
  for line in filename:
    print(f"Line {line_number}: " + line.rstrip())
    line_number += 1

print("\n\n-----------Making a list of lines with readlines( )----------------\n\n")

filename = 'Files Samples/pi_digits.txt'

with open(filename) as new_file_object:
  lines = new_file_object.readline()

print(lines)

for line in lines:
  print(line.rstrip())

print("\n\n-----------Printing the digits with a loop----------------\n\n")

# filename was declared before so I won't do it anymore

with open(filename) as file_object_2:
  new_lines = file_object_2.readlines() # we store each line in a list

complete_string = '' # Create a variable to store the digits

for line in new_lines:
  complete_string += line.strip()#To remove whitespaces at left and right

print(complete_string)
print(len(complete_string[2:])) # prints the length of the decimal places from the third digit forwards, i.e it excludes '3.' -  Remember that this range is inclusive-exlusive. This returns 30, the number of decimal digits we have

print("\n\n-----------Search my Birth day in Pi----------------\n\n")

# I have a text file with first one million digits of pi

pi_million = 'Files Samples/pi_million_digits.py'

with open(pi_million) as file_object_3:
  lines = file_object_3.readlines()

pi_string = ''

for line in lines: # Creates a single string with all the digits of Pi
  pi_string += line.strip()

birthday = input("Enter your name as YYmmDD: ")

if birthday in pi_string: # if your birthday is in the string
  print(f"Yes! You birth day is in the first million pi digits: {birthday}")
  print(pi_string.find(birthday)) # Prints the index where it fins your birthday, you can use both index() or find()
else:
  print("Not so lucky, seems your birthday is quite weird, tho")


