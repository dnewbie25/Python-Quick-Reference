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
