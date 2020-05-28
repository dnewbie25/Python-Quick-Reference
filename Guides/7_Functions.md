# Functions

A function is a miniprogram that you can reuse anytime you want. As a good practice and to make your code maintainable, a function should perform one and only one task. Many people will try to make a single function perform every part of the code, but no, you should have a function per task to complete in a program.

Its syntax is simple:

~~~python 
def my_function():  # Here you define a function that prints 'Hello World'
  print("Hello World")
  
my_function() # This will execute the function you defined
~~~

print( ), len( ), range( ), lower( ) all are examples of functions that are included in Python.

## Parameters and Arguments

This could be tricky at first, but let's create a function to better explain the difference.

~~~python
def hello(name):  # Here you define a function with the Parameter name
  print("Hello, " + name)
  
hello("Alice")  # Here you pass the agument 'Alice' to the parameter name, which is equal to define a normal variable, name = 'Alice'
hello("Rachel") # The same here, you pass the argument 'Rachel' to the parameter name, like name = 'Rachel'
~~~

The last two lines are called 'Calling' a function. Anytime you want to use a function you need to 'call' it in your program. Otherwise, just defining (creating) your function won't make anything by itself.

You can define as many paratemers as you want, just use **def my_parameters(par1, par2, par3, par4):** and so on.

### Define A Default Parameter Value

If you want your function to start with a default value you can just set the parameter as if it were a regular vairiable, like this:

~~~python
def my_function(country = "Norway"): # The default value is 'Norway'
  print("I am from " + country)

my_function("Sweden") # Prints 'I am from Sweden'
my_function("India")
my_function() # If you don't enter an argument it will print 'I am from Norway'
~~~

## Return Values

Sometimes you don't want your function to print the output directly because you need that output to do something else, like saving it into a new variable. Here is were **return** values come into play. 

Let's create an example for this:

~~~python
def get_musician_name(first_name, last_name): # Define a function with 2 parameters
  fullname = f"{first_name} {last_name}"
  return fullname.title() # Capitalize just the first letter of each word
  
musician = get_musician_name("dana", "smith") # Here you save the returned value into the variable musician
print(musician) # This one prints 'Dana Smith'
~~~

### Making An Argument Optional

Sometimes it would be necessary to make an argument optional, like when filling out full names. Some people have a middle name and some don't. This code it's a perfect example, because all you need is to declare the paremeter with an =''.

~~~python
def get_full_name(first_name, last_name, middle_name=''): # middle_name is declared as an empty string
   if middle_name != '':  # If middle_name is no longer empty, then it'll be added to the full name
      full_name = f"{first_name} {middle_name} {last_name}"
   else:
      full_name = f"{first_name} {last_name}"  # Otherwise just first_name and last_name will be printed
   return full_name.title() # In case the user enters a wrongly capitalized word

name = get_full_name("Martha", "Stewart", "Carrey")
print(name)
~~~

## Local and Global Scope

As with any other programming language, a **local** variable is the one you can find inside a function, which can be used by that specific funtion only. No other function can access or modify it.

A **global** variable is declared outside of any function, so every statement in your program can access it and modify its value at any time.

## Exception Handling

This subject has a chapter completely dedicated to how to handle exceptions in our code. But, to summarize, when using functions you can create an exception rule in case the function execution encounters an error. This way the program won't crash but will handle the exception in order to continue executing.

The basic form of en exception is the **try...except** statement. But in order to use this statement you must first know the error you want to avoid.

For instance, if you divide a number by zero in Python, you would get a 'ZeroDivisionError:'. This is the error's name. You want to use this error name when creating the exception. Let's just make a simple code to show it:

~~~python
def spam(divideBy):
 try:
  return 42 / divideBy
 except ZeroDivisionError:
  print('Error: Invalid argument.')

print(spam(42)) # Prints 1
print(spam(150)) # Prints 0.28
print(spam(0)) # Prints 'Error: Invalid argument.' --> This would allow your program to continue executing without crashing
~~~
