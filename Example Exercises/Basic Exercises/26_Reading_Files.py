
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