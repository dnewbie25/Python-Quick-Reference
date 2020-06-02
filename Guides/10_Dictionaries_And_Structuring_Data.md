# Dictionaries And Structuring Data

A dictionary could be the same as a list, but it has one feature that makes it useful when modelling real-world problems, you can create a **key** and associate it with a specific value. It's by definition, a collection of key-value pairs.

**Key-value pairs** are the basics, the all-you-need for dictionaries. You create a key that you can think of it as a variable, and associate that key to a specific value, but inside a list-like data type:

~~~python
alien = { 'color' : 'grey' } # You create a dictionary with braces { }, 'color' is the key and the color grey is the value
~~~

That's the basic structure of dictionaries. You can put more key-value pairs by separating them with a comma ',' to better represent the object you want:

~~~python
alien = { 'color' : 'grey', 'life points' : 120, 'weapon' : 'railgun'} # Here you see a dictionary with 3 key-value pairs
~~~

You can create an empty dictionary by defining it, as if it were a normal list: 

~~~
alien = {}
~~~

## Accessing Keys And Values

#### Values

You can access a value as if it were an element in a regular list by using [ ], but, you need to specify the key, not the index.

~~~python
alien = { 'color' : 'grey', 'life points' : 120, 'weapon' : 'railgun'} # Here you see a dictionary with 3 key-value pairs
print(alien['color']) # Prints 'grey'

# You can even create variables with keys

new_life_points = alien['life points']
print(f"You alien has {new_life_points} life points. Find cover!!") 
~~~

### get( ) - Access Values

You can also get the value of a pais by using the **get( )** method. This one could be very useful because it allows you to put a fallback option in case the key doesn't exist, just use it as a second argument like **dictionary.get(key, optional_argument)**.

~~~python
# First, let's take a look at what would happen if the key doesn't exist
alien = {'color' : blue, 'size' : 'giant'}
print(alien['weapon']) # This one would print 'KeyError: 'weapon'' because there's no such key in the dictionary

# Now, using get( ) it would look like this
alien = {'color' : blue, 'size' : 'giant'}
select_alien = alien.get('weapon', 'No weapon assigned')
print(alien.get()) # Prints 'No weapon assigned', but in this case it won't cause an error
~~~

#### Keys

## Adding New Key-Value Pairs

You can add a new key-value pair by just creating it. Think like you want to access to a value that hasn't been created yet...in lists you would get an IndexError, but in dictionaries you will end up creating that key-value pair. Let me show you with this example, where I'll add the X and Y position of the alien in the screen:

~~~python
alien = { 'color' : 'grey', 'life points' : 120, 'weapon' : 'railgun'}
alien['x-position'] = 12
alien['y-position'] = 120

print(alien) # Prints { 'color' : 'grey', 'life points' : 120, 'weapon' : 'railgun', 'x-position' : 12, 'y-position' : 120}
~~~

**NOTE:** Dictionaries retain the order in which they were created.

## Modifying Values

To modify a value all you need to do is call the key of the dictionary and change the value:

~~~python
alien = {'color' : 'grey'}
print(f"The color is {alien['color']}") # Prints 'The color is grey'

alien['color'] = 'yellow' # Take the key and just change the value, like when you change the value of a normal vairable by re-declaring it
print(f"The color is {alien['color']}")  # Prints 'The color is yellow'
~~~

Let's show you how all of the above topics can be used in a real-worl problem...in this case, I'll keep with the alien stuff.

Let's say you want to control the speed of the alien in the screen (assume we are playing Space Invaders):

~~~python
# Create a dictionary with the position in X and Y axis and the speed
alien = {'x_position': 0, 'y_position': 25, 'speed': 'medium'} 
print(f"Original position: {alien['x_position']}")

# We want our alien to move to the right, so we initialize the variable for the X axis
x_increment = 0

# Depending on the actual speed the alien would move a certain distance. More speed, more increment

if alien['x_position'] == 'slow':
  x_increment = 1
elif alien['x_position'] == 'medium':
  x_increment = 2
else:
  x_increment = 3

# The new position will be the old position plus the increment...yup, that's how it works in real life arcade games
alien['x_position'] = alien['x_position'] + x_increment

print(f"New alien's position is: {alien['x_position']}")
~~~

## Removing Key-Value Pairs

If you don't need a piece of information anymore you can use the **del** statement to get rid of that key-value pair:

~~~python
alien = { 'color' : 'grey', 'life points' : 120, 'weapon' : 'railgun'}

del alien['weapon']
print(alien) # Prints { 'color' : 'grey', 'life points' : 120}
~~~

## Looping Through A Dictionary

You can use a ***for*** loop as with any regular list, but there are a couple of useful ways to use it with dictionaries.

#### items( ) - Loop through each key and value

If you need to output the key and the value of each dictionary's elements, you can use one of the following two approaches:

~~~python
favorite_languages = { 
  'Tim' : 'Spanish',
  'Martha' : 'Finnish',
  'Lucy' : 'German'}
  
# The logical approach

for key in favorite_languages:
  print(f"{key}'s favorite language is {favorite_languages[key]}") # Prints, for example, 'Tim's favorite language is Spanish'
  
# Using items( )

for key, value in favorite_languages.items(): 3 Creates a 'key' and a 'value' variable for keys and values respectively
  print(f"{key}'s faovrita language is {value}") # Prints the same as the above, but is more easy to read
~~~

#### keys( ) - Loop through all Keys

If you want to work just with the keys and don't need the values yet, **key( )** is the method to use.

~~~python
favorite_languages = { 
  'tim' : 'Spanish',
  'martha' : 'Finnish',
  'lucy' : 'German'}
  
# Loop through keys, prints them and change the case

print("My students are :")

for names in favorite_languages.keys(): # Creates a 'names' variable
  print(f"\n {names.title()}") # Capitalize each name
~~~

**NOTE:** Also. keep in mind that when looping through a dictionary, the default looping in Python is the **keys( )**, so even if you don't put the keys( ) at the end, python will assume you need the keys only:

~~~python
print("My students are :")

for names in favorite_languages: # See that we don't need to use the keys( )
  print(f"\n {names.title()}") # Capitalize each name
~~~

#### Sorting Keys In A Loop

Remember that a dictionary will keep is order when you try to print it with a loop, so, in order to sort your dictionary we can use a previous function that doesn't modify the original list while sorting...**sorted( )**:

~~~python
programming_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
 
 # We want to print this list sorted
 
 for names in sorted(programming_languages.keys()):
  print(f"{names.title()}, thanks for telling us your favorite language")
# This will print in the following order:
 Edward, thanks for telling us your favorite language
 Jen, thanks for telling us your favorite language
 Phil, thanks for telling us your favorite language
 Sarah, thanks for telling us your favorite language
~~~
