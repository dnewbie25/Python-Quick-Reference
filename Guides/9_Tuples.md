# Tuples

Technically speaking, *Tuples* are lists, but the article about lists was already too long to include more. So I decided to split it up in three sections, mostly because *Tuples* and the next one, *Dictionaries*, have their ways to work with.

A tuple is a list where the inner values can't be modified. Lists or arrays allow you to change every value at any index whenever you want, but **tuples are immutable**.

## Creating A Tuple

You create a tuple the same way as you would create a regular list but with parenthesis instead or square brackets:

~~~python
my_tuple = (1,2,3,4,5,6)
~~~

Now, different from a list, if you want to create a **tuple with only one element, you must put a comma ',' after the value**, or if you want to create an **empty tuple** you put just the parenthesis.

~~~python
my_element = (3,) # Creates a tuple of only one element

my_empty = ( ) # Creates an empty tuple
~~~

If you try to change any value you will get an error:

~~~python
dimensions = (200, 50)
dimensions[0] = 250 3 Try to change the value at index 0

# You will get this error

Traceback (most recent call last):
 File "dimensions.py", line 2, in <module>
 dimensions[0] = 250
TypeError: 'tuple' object does not support item assignment
~~~

## Looping Tuples

You can loop through a tuple the same way as with a list. Literally.

~~~python
dimensions = (200, 50)
for dimension in dimensions:
 print(dimension) 
~~~

## Writing Over A Tuple

You can't modify a tuple. But you can redefine the entire tuple...which is not convenient all the time, so be careful with this:

~~~python
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
 print(dimension)
 
# As you can see below, we can't modify a tuple like we can modify lists, but we can basically redefine it from zero

dimensions = (400, 500)
print("New dimensions:")
for dimension in dimensions:
 print(dimension)
~~~

**NOTE:** Use Tuples when you want to store a set of values that should not be changed throughout the program.
