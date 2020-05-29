import random

print("You'll play 5 rounds of Rock, Paper and Scissors against the machine")

tries = 0 # Initialize the counters
wins = 0
losses = 0
ties = 0

while tries < 5: # 5 attempts
  print("Choose rock (r), paper (p) or scissors (s) by pressing the respective key")

  computer_choice = random.randint(0,3) # Will choose from 0 to 2 inclusive

  if computer_choice == 0:
    print("Computer chose Rock")
  elif computer_choice == 1:
    print("Computer chose Paper")
  else:
    print("Computer chose Scissors")

  player_choice = input() # Player makes her choice

  if player_choice == 'r':
    print("Player chose Rock")
  elif player_choice == 'p':
    print("Player chose Paper")
  elif player_choice == 's':
    print("Player chose Scissors")
  else:
    print("You loose 1 chance, try again") # If player enters a wrong key, they game will start again, with one attempt less
    tries += 1
    continue

  # Here comes the tricky part. Create the rules and add wins, losses or ties

  if player_choice == 'r': # Player chooses Rock
    if computer_choice == 0: 
      print("It's a tie\n")
      ties += 1
    elif computer_choice == 1:
      print("You loose\n")
      losses += 1
    else:
      print("You win\n")
      wins += 1
  elif player_choice == 'p': # Player chooses Paper
    if computer_choice == 0:
      print("You win\n")
      wins +=1
    elif computer_choice == 1:
      print("It's a tie\n")
      ties += 1
    else:
      print("You loose\n")
      losses +=1
  else:      # Player chooses Scissors
    if computer_choice == 0:
      print("You loose\n")
      losses += 1
    elif computer_choice == 1:
      print("You win\n")
      wins += 1
    else:
      print("It's a tie\n")
      ties += 1


  tries+=1

# Announces the winner of the 5 matches

print(f"Score: Wins {wins}, Losses {losses} and Ties {ties}") # Scoreboard

if wins > losses:
  print("You ROCK!!! You win agains the computer, genius")
else:
  print("You lost everything :(")