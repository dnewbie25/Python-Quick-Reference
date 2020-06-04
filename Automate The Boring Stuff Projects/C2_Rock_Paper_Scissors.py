import random, sys

# Create the computer's choice

def computer():
  choice = random.randint(0,2)

  if choice == 0: # Rock
    return 'rock'
  elif choice == 1: # Paper
    return 'paper'
  else:   # Scissors
    return 'scissors'

# Player inputs her choice

def player():
  choice = input("\nEnter rock (r), paper (p), scissors (s) or 'q' to quit: ")

  if choice == 'q' or choice == 'Q':
    sys.exit()
  elif choice == 'r' or choice == 'R':
    return 'rock'
  elif choice == 'p' or choice == 'P':
    return 'paper'
  elif choice == 's' or choice == 'S':
    return 'scissors'
  else:
    print("Wrong value. Try again") # If the user enters an invalid value, this will send False
    return False

# Determine if the player wins, losses or ties

def match(user, machine):

  if user == False: # If user enters an invalid character
    return 'failed'
  elif user == 'rock': # Player chooses ROCK
    if machine == 'rock':
      return 'tie'
    elif machine == 'paper':
      return 'loose'
    else:
      return 'win'
  elif user == 'paper': # Player chooses PAPER
    if machine == 'rock':
      return 'win'
    elif machine == 'paper':
      return 'tie'
    else:
      return 'loose'
  else:   # Player chooses SCISSORS
    if machine == 'rock':
      return 'loose'
    elif machine == 'paper':
      return 'win'
    else:
      return 'tie'

# Gameplay, 5 rounds

attempts = 0
wins = 0
losses = 0
ties = 0

while attempts < 5:
  user_input = player()
  computer_input = computer()

  play_round = match(user_input, computer_input)

  if play_round == 'failed':
    print("Invalid input. Loose 1 attempt")
    attempts+=1
  elif play_round == 'win':
    print(f"Player choose: {user_input.title()}")
    print(f"Computer choose: {computer_input.title()}")
    print("\nYou win this one!")
    wins+=1
    attempts+=1
  elif play_round == 'loose':
    print(f"Player choose: {user_input.title()}")
    print(f"Computer choose: {computer_input.title()}")
    print("You lost this one")
    losses+=1
    attempts+=1
  else:
    print(f"Player choose: {user_input.title()}")
    print(f"Computer choose: {computer_input.title()}")
    print("It's a tie")
    ties+=1
    attempts+=1

# Determines the winner

print(f"\nFinal Score: Wins {wins}, Losses {losses} and Ties {ties}")

if wins > losses:
  print("\nCongrats!! You won")
elif wins < losses:
  print("\nYou LOST everything")
else:
  print("It's a tie -_-")