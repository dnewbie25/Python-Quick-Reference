spam = ['apples', 'bananas', 'tofu', 'cats', 'avocado', 'pets', 'parrots']

# Function that returns a string with list's values separated by a comma except the last one, which should be separated by an ' and'

def comma_code():
  index = 0

  while index < (len(spam)):
    if index < (len(spam) - 2): # Uses the comma 2 items before the last one
      print(f"{spam[index]}, ", end='')
    elif index < (len(spam) - 1): # Uses no comma with the penultimate item
      print(f"{spam[index]} ", end='')
    else:  # Prints the last item separated by an ' and' from the penultimate item
      print(f"and {spam[index]}")
    
    index += 1

comma_code()