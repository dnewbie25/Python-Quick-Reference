#########################  Dictionary Inside List #############################

# Create a dictionary with the characteristics of an alien

alien = {'color' : 'grey', 'life points' : 50, 'speed' : 'slow'}

# Create a list and append 30 aliens to it
all_aliens = [ ]

for number_of_aliens in range(30): # Will loop 30 times 
  all_aliens.append(alien) # Appends the alien dictionary to the list
  
# Let's test how many copies we have of the first alien dictionary
for copies in all_aliens[0:5]: # Loops through the first 5 elements and prints them
  print(copies)
  
# Print the total of aliens
print(f"\nThe total of aliens is : {len(all_aliens)}\n\n")

''' We can even change the values of the n first elements if we want to '''
# Create a list for green aliens
green_aliens = []

# Insert the characteristics of a new alien defined in a dictionary
for alien in range(30):
  a_new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
  green_aliens.append(a_new_alien)

# Change the color and the speed of first 7 aliens
for alien in green_aliens[0:7]:
  if alien['color'] == 'green':
    alien['color'] = 'yellow'
    alien['points'] = 10
    alien['speed'] = 'medium'

# Show the first 10 aliens
for alien in green_aliens[0:10]:
  print(alien)

print(len(green_aliens))

########################### List Inside Dictionary #################################

ingredients = {'dough' : ['corn powder', 'flour'],
                'toppings' : ['lettuce', 'cheese', 'pineapple'],
                'sauce' : ['tomatoe', 'napolitan', 'alfredo']}
 # Print the order
print(f"You ordered a pizza with {ingredients['dough'][0]} dough and with these toppings:")
 
for topping in ingredients['toppings']:
  print(topping)

####################### Dictionaries Inside Dictionaries ######################################
print("\n\n")
my_users = {
    'dphilip89' : {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
     'rachelAm' : {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        }, # It's a good practice to put a comma at the end of your last dictionary when doing this nesting
 }
 
for username, info in my_users.items(): # Loop through the parent dictionary. The 'info' variable would be equal to the nested dictionaries
  print(f"\nUsername: {username}")
  print("Information: ")
  
  full_name = f"{info['first'].title()} {info['last'].title()}"  # The 'info' variable holds the values, which are other dictionaries
  location = f"{info['location']}"
  
  print(f"\t\tFull name: {full_name}")
  print(f"\t\tLocation: {location.title()}")