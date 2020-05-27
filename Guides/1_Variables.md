# Variables

In Python variables can be assigned by using a simple assignment operator '='.

~~~python
my_variable = "Some variable"
~~~

A variable can be an **Integer, Float, String, Boolean**.

~~~python
my_integer = 10 # Numbers WITHOUT a decimal part

my_float = 10.54 # Numbers WITH a decimal part

my_string = "My String" # A set of characters between quotes, it can include numbers, i.e. "My string #1"

my_bool = True # Used in boolean algebra. It can be True or False
~~~

## Integer and Floats

They represent integer or decimal numbers. You can operate with them, but if you combine *Integers* and *Floats* you will get a *Float* as the result of the specified operation. Also, all divisions will give you a *Float* result.

If you want to keep a number as an *Integer* you can use the following methods:

### int() and float()

They convert a number to the specified data type:

~~~python
int_to_float = float(10) # Prints 10.0

float_to_int = int(10.56) #Print 10, removing the decimal part
~~~

## Strings

### str()

This can turn a number into a string so you can concatenate strings without any class error, since you can't add text and numbers:

~~~python
print("Print this " + str(1020) + "as text") # Prints 'Print this 1020 as text'

print("Print this " + 1020 + "as text") # This will throw an error. Python would think you are trying to get the sum of words and letters
~~~

### print()

This is how you'll make everything be dsplayed by the console.

~~~python
print("Something to print")
~~~

## How to know the data type of a variable

### type()

With type() you can know the data type of a specific variable.

~~~python
type(10) # Prints <class 'int'>

type(10.56) # Prints <class 'float'>

type("String") #Prints <class 'str'>

type(False) # Prints <class 'bool'>
~~~

type() can also be used to know if the specified parameter is a list, a tuple, even a dictionary. More about this in their respective sections.

## Final tips and reminders:

### Multiple assignment

You can create a single line with all of your variables.

~~~python
x, y, name, is_cool = (1, 2.5, 'John', True)
~~~

### Basic math

You can use math within a variable. 

~~~python
a = x + y
~~~

### Casting

You can assign a value to a variable and change its data type at the same time.

~~~python
x = str(x)
y = int(y)
z = float(y)
~~~
