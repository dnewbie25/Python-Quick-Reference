# Creates the collatz function

def collatz(number):
  if number % 2 == 0: # If even
    return number // 2
  else: # If odd
    return number * 3 + 1

# User enters a number

def user_input():
  number = int(input("Enter an integer number: "))
  return number

# Loops until it returns 1

def collatz_loop():
  value = user_input() # assigns the user's input to a variable
  result = collatz(value) # creates an initial collatz with the user's input
  while result >= 1:
    if result != 1: # While result is different from 1 it continues looping
      print(result)
      result = collatz(result)
    else: # If result is equal to 1 it stops
      print(result)
      break

collatz_loop()
