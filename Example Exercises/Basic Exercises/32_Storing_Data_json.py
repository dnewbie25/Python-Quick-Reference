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