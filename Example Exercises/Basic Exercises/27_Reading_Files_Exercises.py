# Reading Learning python.txt

filename = 'Files Samples/Learning python.txt'

# Reading the entire file

with open(filename) as method_1:
  print_line = method_1.read()

print(print_line)

print("\n------------------------------------\n")

# Looping over the file object

with open(filename) as method_2:
  for line in method_2:
    print(f"{line.rstrip()}")

print("\n------------------------------------\n")

# Loop over file as a list

with open(filename) as method_3:
  print_line = method_3.readlines()

for line in print_line:
  print(f"{line.strip()}")


print("\n------------------------------------\n")

'''Here I'll replace the start of each line by a hyphen'''

with open(filename) as replace_method:
  print_line = replace_method.readlines()
  
for line in print_line:
  print(f"{line.replace('In Python you can...', ' - ').strip()}")