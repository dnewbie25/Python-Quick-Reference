# Modules

This could be a pretty extensive topic, so I'll put it as simple as I can. A module is a library, it means a set of pre-built functions. They could be created by the Python team or by indie developers in order to help Python community to solve usual problems.

The basic syntax for a module is **import *NameOfModule***. This one should be placed at the start of the file or before the part of the program you want the module to be used:

~~~python
import random # The import is the basic structure. This one imports the random module so you can use its functions to create random numbers, order lists or strings randomly among other useful functions
for i in range(5):
 print(random.randint(1, 10)) # random.randint() is a function from the random module. It takes a random integer between the specified range inclusive [1,10]
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

## Storing Your Functions in Modules

You can create functions to reuse in a lot of programs just like Python's built-in functions. You can do this by creating a module for that function. For this you need to do the following:

#### 1 - Create A Module:

A module is a *.py* file, just like any other python file we have been using.

For example, we will create a module called *pizza.py*. This would be the file storing our module. Inside this file we must add one or more funtions:

~~~python
# Create a function. Try to use a different name from the file's name
def make_pizza(size, toppings): # The funtions has two parameters for size and toppings
 # Summarize the pizza you want to make
 print(f"\nMaking a {size}-inch pizza with the following toppings:")
 for topping in toppings:
  print(f"- {topping}")
~~~

Now we save the file in the same directory of our the program we are creating that needs the *pizza.py* module.

#### 2 - Using A Module:

Just like with Python's own modules, we just simply import the module.

Imagine our program is called *baking_pizzas.py*. We don't want to write a funtion that summarizes the pizza ordered by the customer because we already created it in *pizza.py*.

The syntax for this is ***Module_Name*.Function_Name(parameters)**.

~~~python
import pizza # This line imports the pizza function inside the pizza.py file, just like any other module

# Now we can just create a pizza by calling the function 'make_pizza' inside the 'pizza.py' file
pizza.make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese') 
pizza.make_pizza(12, 'pepperoni')
~~~

### Importing Specific Functions

If you need just a specific set of functions from a module, you can import them with the statement:

**from *module_name* import *function_name1, function_name2, function_name3***

~~~python
from pizza import make_pizza

# With the above instruction you don't need to wrte pizza.make_pizza() when calling the function. Python would know what function are you refering to
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
~~~

### as - Give An Alias to a *Function*

If you think the name of a specific function from a module could lead to a misunderstanding when reading the code, you can change its name by using:
~~~python
from pizza import make_pizza as creating_pizza

creating_pizza(16, 'pepperoni') # You just change the functions name, not its functionality
~~~

### as - Give An Alias to a *Module*

Now, if you have modules that share the same name or if you just simply want to use an easy to remember name, you can change the name of an entire module:

~~~python
import pizza as pizza_order # You can't for 'from X import Y' with this method, you need to import the entire module

pizza_order.make_pizza(13, 'alfredo sauce') # Changes the module name but not the functions inside it
~~~

### * - Importing All Functions from a Module

If you don't want to use the *Module_Name.Function_Name()* notation you can use *from* to import all functions so you can just use the functions name:

~~~python
from pizza import *  # Imports all functions

make_pizza(48, ' cheese', 'pineapple', 'basil') # You can now use the function by calling it by its name
~~~

Although it could be easy to work with this instruction, it's better not to use with modules you didn't write yourself in order to not create conflicts with the functions you and the other people defined.
