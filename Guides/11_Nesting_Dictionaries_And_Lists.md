# Nesting Dictionaries And Lists

Lists and dictionaries are powerful because you can and eventually you'll use a combination of both, whether you are nesting a list inside a dictionary of a dictionary inside a list.

## Dictionary Inside List

One example of how you can do that could be creating a lists of characters, like in the Space Invaders game, where you can create an alien and replicate it as many times as you want in a list:

~~~python
# Create a dictionary with the characteristics of an alien

alien = {'color' : 'grey', 'life points' : 50, 'speed' : slow}

# Create a list and append 30 aliens to it
all_aliens = [ ]

for number_of_aliens in range(30): # Will loop 30 times 
  new_alien = all_aliens.append(alien) # Appends the alien dictionary to the list
  
# Let's test how many copies we have of the first alien dictionary
for copies in new_alien[0:5]: # Loops through the first 5 elements
  print(copies)
  
# Print the total of aliens
print(f"\nThe total of aliens is : {len(new_alien)}")
~~~

**What if we want to create a list of 30 aliens and modify the first 7 of them?**

~~~python
# Create a list for green aliens
green_aliens = []

# Insert the characteristics of a new alien defined in a dictionary, 30 times
for alien in range(30):
  a_new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
  green_aliens.append(a_new_alien)

# Change the color and the speed of first 7 aliens
for alien in green_aliens[0:7]:
  if alien['color'] == 'green':
    alien['color'] = 'yellow'
    alien['points'] = 10
    alien['speed'] = 'medium'

# Show the first 10 aliens, with the first 7 of them changed to yellos, 10 points and with medium speed
for alien in green_aliens[0:10]:
  print(alien)

print(len(green_aliens)) # Make sure we still have 30 aliens
~~~

## List Inside Dictionary

A good example would be creating a dictionary with ingredients for a pizza. If we use just a dictionary, we could store only toppings, or dough types, or sauces...well, you can put all of this in one single dictionary but you will confuse yourself. You need order when declaring things and not mix different stuff no matter if they belong to the same product. For example:

~~~python
# Create a list of pizza ingredients in a dictionary, no more

ingredients = {'dough' : 'corn powder','sauce' : 'tomatoe','sauce':'alfredo','topping' : 'lettuce','topping' : 'cheese','topping' : 'pineapple','dough' : 'flour','sauce' : 'napolitan} # As you can see, there are many kinds of elements mixed together

# A better way, lists inside a dictionary

ingredients = {'dough' : ['corn powder', 'flour'],
                'toppings' : ['lettuce', 'cheese', 'pineapple'],
                'sauce' : ['tomatoe', 'napolitan', 'alfredo']}
 # Yes, it could take more time to create a dictionary like this, but you'll save hours when looking for a specific element. Planning is the key to success
~~~

