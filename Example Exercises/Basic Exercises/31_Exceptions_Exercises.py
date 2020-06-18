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
see_this = 'Files Samples/Merma-*-ids.txt'

for items in filenames:

  try:

    for i in range(3):
      with open(items, 'a') as f:
        content = input("Enter the name of your pet: - ")
        f.write(content + "\n")
  except OSError:
    print(f"{items} does not exist")



