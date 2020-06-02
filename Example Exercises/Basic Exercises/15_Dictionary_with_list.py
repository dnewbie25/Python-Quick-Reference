# We have a dictionary of favorite languages

favorite_languages = { 
  'tim' : 'Spanish',
  'martha' : 'Finnish',
  'lucy' : 'German',
  'sara' : 'Greek'
  }

# We have a list of students with the same favorite languages as us

my_favorite = ['Greek', 'Spanish']

# Evaluate if they have the same favorite language

for names, languages in favorite_languages.items(): # Loop through keys and values
  for my_language in my_favorite: # While looping through idctionary it also loops through my list
    if languages == my_language: # If we love the same language, it'll print this
      print(f"Hey, {names.title()}, we both love {my_language}")