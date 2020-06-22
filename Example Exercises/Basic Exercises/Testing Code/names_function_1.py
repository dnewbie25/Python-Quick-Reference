# This will serve as a module for the 2 program

def get_formatted_name(first_name, last_name, middle_name=''):
  """Generate a neatly formatted full name"""
  if middle_name: # If it's not empty and it's not a Falsy value
    full_name = f"{first_name} {middle_name} {last_name}"
  else: # If the person does not have a middle name
    full_name = f"{first_name} {last_name}"
  return full_name.title()