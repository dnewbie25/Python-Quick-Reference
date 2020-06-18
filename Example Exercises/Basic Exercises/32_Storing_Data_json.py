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

