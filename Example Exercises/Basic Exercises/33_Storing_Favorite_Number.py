import json

###### Favorite Number ###########

def favorite_number():

  filename = 'user_favorite_number.json'

  try: # Try to open the file
    with open(filename) as f:
      fav_number = json.load(f)
  
  except FileNotFoundError: # If the file does not exist
    try: # Enter a number
      fav_num = int(input("Enter your favorite number: "))
    except ValueError: # If user enters a invalid input
      print("Please enter a number")
    else: # Once they enter a correct value dump it to the json file
      with open(filename, 'w') as f:
        json.dump(fav_num, f)
  else: # If the file was initially open without issues then returns the data it has stored
    print("My favorite number is already stored, it is " + str(fav_number))

favorite_number()

print("\n\n---------------------Username validation----------------\n\n")

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

  if username: 
    print(f"Hi {username}...is this you?")
    validation = input("Enter yes or no: ")
    if validation.lower() == 'yes':
      print(f"Welcome back, {username}")
    elif validation.lower() == 'no':
      print("Then enter your username")
      new_username = get_new_user()
      print("We'll remember you now!!"  + new_username)
  
greet_user()