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

