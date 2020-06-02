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

## Accessing Values

You can access a value as if it were an element in a regular list by using [ ], but, you need to specify the key, not the index.

~~~python
alien = { 'color' : 'grey', 'life points' : 120, 'weapon' : 'railgun'} # Here you see a dictionary with 3 key-value pairs
print(alien['color']) # Prints 'grey'

# You can even create variables with keys

new_life_points = alien['life points']
print(f"You alien has {new_life_points} life points. Find cover!!") 
~~~

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
