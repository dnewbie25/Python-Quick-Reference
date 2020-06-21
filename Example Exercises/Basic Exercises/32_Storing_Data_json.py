import json

'''Store data in json file'''

numbers = [1, 2, 3, 4, 5, 6, 7]

filename = 'Files Samples/numbers.json'

with open(filename, 'w') as file_object:
  json.dump(numbers, file_object)



'''load data from json file'''

filename_2 = 'Files Samples/numbers.json'

with open(filename_2) as json_file: # Opens the file and put it an alias
  numbers_2 = json.load(json_file) # Create a numbers object equals to the json_file

print(numbers_2) # Prints [1, 2, 3, 4, 5, 6, 7]


########################################################
########################################################

'''We can refactor the following function'''

'''

def greet_user():
  ### greet the user ##
  filename = 'usernames.json'

  try:
    with open(filename) as f:
      username = json.load(f)
  except FileNotFoundError:
    username = input("What's your username?: ")
    with open(filename, 'w') as f:
      json.dump(username, f)
      print(f"We'll remember you when you come back, {username}")
  else:
    print(f"Welcome back, {username}")

greet_user()

'''

# When refactoring we can just split the function into mini functions that perform one task. Each function should return either the expected value or None. No ambiguity

# The previous function has this elements: try to open the file, if the file does not exists then creates a file, after that load the file and greet the user

'''We can create three mini functions. Each one should deal with one and only one of those 3 subproblems'''

def get_stored_username():
  """Get the stored username"""
  filename = 'Files Samples/username.json'
  try: # Try to open the file
    with open(filename) as f:
      username = json.load(f)
  except FileNotFoundError:
    return None # It should return None if the file does not exists
  else:
    return username # If it exists then return the username

def get_new_user():
  """If get_stored_name() returns None this one should ask for a username"""
  username = input("Enter your username: ")

  filename = 'Files Samples/username.json'

  with open(filename, 'w') as f: # Creates a file and dump the username
    json.dump(username, f)

  return username

def greet_user():
  """This function grets the user"""
  username = get_stored_username() # Try to read the username

  if username: # If username returns something that's not a Falsy value, if you put 'username == True' this is a strict equality so it won't work
 
    print(f"Welcome back, {username}")
  
  else: # Remember False values are 0, 0.0, None, empty strings or empty lists 
    username = get_new_user() # Input a new username
    print(f"We'll remember you when you come back, {username}")

greet_user()