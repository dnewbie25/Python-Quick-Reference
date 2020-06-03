# We have a dictionary of favorite languages

favorite_languages = { 
  'tim' : 'Spanish',
  'martha' : 'Finnish',
  'lucy' : 'German',
  'sara' : 'Greek'
  }

# We have a list of students with the same favorite languages as us

my_favorite = ['Greek', 'Spanish', 'Latin', 'Japanese']

# Evaluate if they have the same favorite language

for names, languages in favorite_languages.items(): # Loop through keys and values
  for my_language in my_favorite: # While looping through idctionary it also loops through my list
    if languages == my_language: # If we love the same language, it'll print this
      print(f"Hey, {names.title()}, we both love {my_language}")

print("\n\n")      

# Rivers

rivers = {'Sepik' : 'New Guinea', 'Mississippi' : 'US', 'Ganges' : 'india'}

for river, country in rivers.items(): # Remember to use items() when using 'key, value' in a for loop
  print(f"The {river.title()} river runs in {country.title()}")
print("\n\n")

for river in rivers.keys(): # Prints just the key, river's name
  print(river.title())
print("\n\n")

for country in  rivers.values():
  print(country.title())
