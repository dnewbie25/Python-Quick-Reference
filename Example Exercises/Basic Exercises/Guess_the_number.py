import random # To generate the random number

random_number = random.randint(0,101) # Random number between 0-100 inclusive

print("You have 10 opportunities to guess the number\n")

tries = 0 # Initialize the counter variable

#Create a loop for 10 tries which counts the number of the attempt

while tries < 10:
  print("Enter your guess, attempt #" + str(tries + 1)) # Counts the number of attempts
  
  my_guess = int(input()) # Converts the input to an integer

  if my_guess < random_number:
    print("Your guess is too low, what about " + str(my_guess+1))
  elif my_guess > random_number:
    print("Your guess is too high, what about " + str(my_guess-1))
  else:
    print("You win!!! " + str(my_guess) + " is the number!")
    break

  tries += 1  # Increase the counter variable, tries = tries + 1



