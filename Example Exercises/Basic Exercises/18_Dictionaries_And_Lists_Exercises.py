# People in a list

person1 = {
  'height' : 180,
  'eyes color' : 'brown',
  'hair' : 'curly',
  'hair color' : 'pink',
  'age' : 25,
  'city' : 'Paris',
  'firts_name' : 'David',
  'last_name' : 'Lopez'
   }

person2 = {
  'height' : 180,
  'eyes color' : 'green',
  'hair' : 'curly and blonde',
  'hair color' : 'brown',
  'age' : 20,
  'city' : 'Medellin',
  'firts_name' : 'Rachel',
  'last_name' : 'Lopez'
   }

person3 = {
  'height' : 180,
  'eyes color' : 'blue',
  'hair' : 'blonde',
  'hair color' : 'red',
  'age' : 45,
  'city' : 'Paris',
  'firts_name' : 'Maria',
  'last_name' : 'Smith'
   }

people_list = [person1, person2, person3]

for person in people_list: # Loops through the people and prints the data with no formatting 
  print(person)
print("\n\n")

# Pets

pet1 = {'animal' : 'fish', 'owner' : 'robert'}

pet2 = {'animal' : 'dog', 'owner' : 'martha'}

pet3 = {'animal' : 'cat', 'owner' : 'richard'}

pet4 = {'animal' : 'parrot', 'owner' : 'monica'}

pets = [pet1, pet2, pet3, pet4]

for animals in pets: # Loops through the pets and prints the naimal and the owner's name
  print(f"The {animals['animal'].title()}'s owner is {animals['owner'].title()}")
print("\n\n")

# Favorite Places

favorite_places = {'dani' : ['guatape', 'providencia'], 
                    'mateo' : ['san andres', 'bolivar'], 
                    'anderson' : ['rionegro', 'los angeles']}

for name, place in favorite_places.items(): # Prints the favorite places of each person
  print(f"{name.title()}'s favorite places are:")
  for each in place:
    print(f"\t{each.title()}")
print("\n\n")

# Favorite Numbers

people_numbers = {
    'bob' : [2,1,5],
    'miriam' : [1,8,4],
    'agatha' : [9,3,6]
}

for names, numbers in people_numbers.items(): # Prints the favorite numbers of each person
  print(f"{names.title()}'s favorite numbers are:")
  for number in numbers:
    print(f"-{number}")
print("\n\n")

# Cities

cities = {
    'bogota' : {
         'country' : 'colombia',
         'population' : 8000000,
         'fact' : 'biggest city in Colombia'
    },
    'new york' : {
        'country' : 'USA',
        'population' : 8300000,
        'fact' : 'city that never sleeps'
    },
    'lima' :{
        'country' : 'peru',
        'population' : 268000,
        'fact' : 'second largest desert capital city'
    }
}

for city, info in cities.items(): # Loops through keys and values
  print(f"{city}:") # Prints the city
  for field, data in info.items(): # Since the values are other dictionaries, it loop through those dictionaries' keys and values
    if data == 'USA': # Print USA in upper case
      print(f"\t{field.title()}: {data.upper()}")
    elif field == 'population': # Prints the population as an integer
      print(f"\t{field.title()}: {data}")
    else: # Capitalize the resto of words' first letter
      print(f"\t{field.title()}: {data.title()}")
