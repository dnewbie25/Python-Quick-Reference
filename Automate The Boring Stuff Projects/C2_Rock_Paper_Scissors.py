import random, sys

# Create the computer's choice

def computer():
  choice = random.randint(0,2)

  if choice == 0: # Rock
    return 'r'
  elif choice == 1: # Paper
    return 'p'
  else:   # Scissors
    return 's'

# Player inputs her choice

def player():
  choice = input("\nEnter rock (r), paper (p), scissors (s) or 'q' to quit: ")

  if choice == 'q' or 'Q':
    sys.exit()
  elif choice == 'r' or 'R':
    return 'rock'
  elif choice == 'p' or 'P':
    return 'paper'
  else:
    print("Wrong value. Try again") # If the user enters an invalid value, this will send False
    return False

# Determine if the player wins, losses or ties

def match(user, machine):
  if user == 'rock': # Player chooses ROCK
    if machine == 'r':
      return 'tie'
    elif machine == 'p':
      return 'loose'
    else:
      return 'win'
  elif user == 'paper': # Player chooses PAPER
    if machine == 'r':
      return 'win'
    elif machine == 'p':
      return 'tie'
    else:
      return 'loose'
  else:   # Player chooses SCISSORS
    if machine == 'r':
      return 'loose'
    elif machine == 'p':
      return 'win'
    else:
      return 'tie'

