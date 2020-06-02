# Dictionary storing a person's info
first_name = 'Danielle'
last_name = 'Monroe'

person = {
  'height' : 180,
  'eyes color' : 'brown',
  'hair' : 'curly',
  'hair color' : 'pink',
  'age' : 25,
  'city' : 'Paris',
  'firts_name' : first_name,
  'last_name' : last_name
   }

print(person)

# Favorite number by creating  a dictionary

people_numbers = {}

i = 0

while i < 5:
  key = input()
  value = int(input())
  people_numbers[key] = value
  i+=1

print(people_numbers)
print("\n\n")

# Glossary 
print("You can create your own glosarry by using the previous loop")

glossary = {}
index = 0

while index < 5:
  print("Enter a word:")
  word = input()
  print("Enter a brief meaning:")
  meaning = input()

  glossary[word] = meaning
  index+=1

for key in glossary:
  print(f"The meaning of {key} is {glossary[key]}")

