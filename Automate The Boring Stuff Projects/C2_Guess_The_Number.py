import random, sys

# Let the computer guess a number
def computer_guess():
  choice = random.randint(0,100)
  return choice

# Let the user choose a number

def player_guess():
  player = input("Enter a number to play or 'q' to exit: ")
  if player == 'q' or player == 'Q':
    sys.exit()
  else:
    player = int(player)
    return player

# Assign the computer choice to a variable

computer_number = computer_guess()

# Initialize the number of attempts
attempts = 0

# Starts gameplay with the outputs
while attempts < 10:
  player_number = player_guess()

  if player_number > computer_number:
    print(f"\nYour guess is too high, what about {player_number-1}")
    attempts+=1
  elif player_number < computer_number:
    print(f"\nYour guess is too low, what about {player_number+1}")
    attempts+=1
  else:
    print(f"\nYes!! {computer_number} is the number. You rock!!")
    break
