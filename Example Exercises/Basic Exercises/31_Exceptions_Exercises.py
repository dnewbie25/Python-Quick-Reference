# Addition

def addition():

  try: # Try to input numbers
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
  except ValueError: # If the input is not a number stop
    print("The input was incorrect. Try again with integer numbers")
  
  print(num1 + num2)

#addition()

print("\n\n-----------------------Addition Calculator------------------\n\n")

# Addition Calculator

while True:
  
  try: # Try to input numbers
    
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    
  except ValueError: # If the input is not a number stop
    print("The input was incorrect. Try again with integer numbers")
  
  else:
    print(num1 + num2)

  
  should_continue = str(input("Do you want to continue? Type Enter to continue or 'q' to quit."))
  if should_continue.lower() == '':
    continue
  elif should_continue.lower() == 'q':
    break
  else:
    print("You enter an invalid value. You are trapped in this loop")


print("\n\n-----------------------Cats And Dogs------------------\n\n")

filenames = ['Files Samples/Cats.txt', 'Files Samples/Merma-*-ids.txt','Files Samples/Dogs.txt']

for items in filenames: # Loops through all the items in the list (3 files)

  try: # Try to open the file and write 3 different names for the pets

    with open(items, 'a') as f:
      for i in range(3):
        content = input("Enter the name of your pet: - ")
        f.write(content + "\n")

  except FileNotFoundError:
    print(f"{items} does not exist")

  except OSError: # If the file does not exists it will send this error. OSError is the parent class of FileNotFoundError. It arises sometimes instead of FileNotFound when using lists. You can't put OSError before FileNotFoundError. You need to go from the specific to the general
    print(f"{items} does not exist")

  



