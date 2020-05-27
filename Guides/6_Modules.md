# Modules

This could be a pretty extensive topic, so I'll put it as simple as I can. A module is a library, it means a set of pre-built functions. They could be created by the Python team or by indie developers in order to help Python community to solve usual problems.

The basic syntax for a module is **import *NameOfModule***. This one should be placed at the start of the file or before the part of the program you want the module to be used:

~~~python
import random # The import is the basic structure. This one imports the random module so you can use its functions to create random numbers, order lists or strings randomly among other useful functions
for i in range(5):
 print(random.randint(1, 10)) # random.randint() is a function from the random module. It takes a random integer between the specified range
~~~

You can import multiple modules at the same time:

~~~python 
import random, sys, os, math
~~~

### Importing Specified Functions

You can also import just specific functions from a module instead of importing all module's functions. Just use:

*from **module_name** import **function_name***

~~~python
from pizza import make_pizza 3 This would work like this in the real world. You just import a function so you don't have to create it from scratch and use it, that's it

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
~~~

Also, you can import all of the functions from a module by using:

*from **module_name** import* * 

~~~python
from pizza import *  # Imports all functions

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
~~~

A good practice is to import just the functions you need. It's really rare to find a program that needs all the functions from a module.
