import random
# Create a list and a function 

coin_flips = []
numberOfStreaks = 0
counter = 0 # Counter for the amount of 'H' or 'T'

for experiment in range(10000) : # 10,000 tries
  print("Loop 3")
  # Code that creates a list of 100 'heads' or 'tails' values.
  for loop in range(100):
    value = random.randint(0, 1) # Random number 0 or 1 generated
    if value == 0:
      coin_flips.append('H')
    else:
      coin_flips.append('T')

  # Code that checks if there is a streak of 6 heads or tails in a row.
  for index in range(len(coin_flips)): # Loops from 0 to 99, which is 100 items
    print("Loop 2") # Used to check the loop is actually executing
    if coin_flips[index] == 'H' and coin_flips[index - 1] == 'H': # If the element before the one evaluated is equel to 'H' it add 1 to counter. If the index is zero, it won't anything with this kind of conditional
      counter += 1
    elif coin_flips[index] == 'T' and coin_flips[index - 1] == 'T': # Same fot the 'T'
      counter += 1
    else: # If the above is False in both cases, it restarts the counter to zero
      counter = 0

    if counter == 6: # If the counter is equal to 6, it means a streak was completed, so it add 1 to numberOfStreaks
      numberOfStreaks += 1  

  coin_flips = [] # Restar the list for the next iteration


print("Chance of streak: %s%%" % (numberOfStreaks / (10000 * 100) * 100)) # Calculates the probability of having streaks in lists of 100 items, 10,000 times
