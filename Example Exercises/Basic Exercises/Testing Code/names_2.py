# Here we'll use the module names_function_1

from names_function_1 import get_formatted_name # We import the function we have in that program

print("Enter 'q' to exit at any time.")

while True:
  first = input("\nPlease enter your first name: ")
  if first == 'q':
    break

  last = input("\nPlease enter your last name: ")
  if last == 'q':
    break

  middle = input("\nDo you have a middle name? If so type it, otherwise press Enter: ")

  formatted_name = get_formatted_name(first, last, middle)
  print(f"\tNeatly formatted name: {formatted_name}")