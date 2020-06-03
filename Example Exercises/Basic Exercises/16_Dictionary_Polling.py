# Create a dictionary with the favorite programming languages of certain people

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

# Create  alist of people missing for saying their favorite language

people_missing = ['max', 'tim', 'sarah', 'rachel', 'thomas', 'phil', 'phillip']

# Create a for loop for every name in the list

# Here you want to use the 'in' or 'not in' statements to loop through the list of people missing and compare the name with the keys of the idctionary

for names in people_missing:
  if names in favorite_languages.keys():
    print(f"\nThank you for responding, {names}")
  else:
    print(f"\nPlease fill up the poll, {names}")

      


  
  
      

      
print(favorite_languages)