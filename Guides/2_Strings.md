# Strings

In the *Variables* section I talked about the **String** data type. Here I will elaborate more about what are strongs, how can you use them and some useful methods to interact with strings.

## What is a String?

A string is a set, a sequence of characters inside single quotes like this *'string'* or double quotes *"like this one"*. As with any other programming language, you must start and finish the string with the same kind of quotation mark.

## What can you do with a String?

Strings have a lot of useful methods to change case, split words, count the number of characters, even to add another string at the beginning or end of another string. I'll list some of the most used methods for strings.

### Changing Case 

**title( )**:

You can capitalize the first letter of each word leaving the rest as lowercase letter:

~~~python
name = "aDA loVElacE"
print(name.title()) # Prints 'Ada Lovelace'
~~~

**lower( )**: Turns everything into lower case, i.e. 'ada lovelace'

**upper( )**: Turns everything into upper case, i.e. 'ADA LOVELACE'

It's a good practice to convert all the input from users into lower case and then changing it to the most appropriate case according to your program's goal.

### Using Variables in a String

There's a couple of ways to use variables in a String. 

**Concatenation**

The most used way is concatenation (which can be used to add a string to a string), by using the '+' operator.

~~~python
my_string = "This is my string #"
my_string2 = " out of 10"
number = 3

print(my_string + str(number) + "my_string2) # Prints 'This is my string #3 out of 10'
# Remember that when using strings and numbers you must use str( ) to convert the numerical values into text
~~~

**Multiplication**

You can repeat a string a number of times by using a asterics. This is the only way to operate a number and a string without using the str( ) method.

~~~python
string = "Time"
number = 3
print(string * number) # Prints 'TimeTimeTime'
~~~

**f-Strings**

This can be compared to a *template literal* in other programming languages. You can get rid of the '+' operator when concatenating variables in a string by usinf **f"{} {}"**.

Let's say you don't want to repeat *string* like in the previous example, and don't want to use '+' nor str( ). You can just do the following:

~~~python
string = "Time"
number = 3
print(f"{string} * {number} is equal to 'TimeTimeTime'") # Prints 'Time * 3 is equal to TimeTimeTime'
~~~

This can be used with functions, and methods if you want to.

~~~python 
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message) # Prints 'Hello, Ada Lovelace'
~~~

### Adding or Removing Whitespaces

**Newline and Tab**

Within a string you can use *\n* or *\t* to add a new line space or a tab line space

~~~python 
print("Languages:\n\tPython\n\tC\n\tJavaScript")
#Prints
Languages:
   Python
   C
   JavaScript 
~~~

**Stripping Whitespaces with rstrip( ), lstrip( ) or strip( )**

**rstrip( )**

Removes whitespace at the right end

~~~python
string = "My python  "
print(string.rstrip()) " Prints 'My python'
~~~

**lstrip( )**

Removes whitespace at the left end

~~~python
string = "  My python"
print(string.rstrip()) " Prints 'My python'
~~~

**strip( )**

Removes whitespaces at both ends

~~~python
string = "  My python  "
print(string.strip()) " Prints 'My python'
~~~

**end=''**

With this little instruction at the end of a **print( )** function you can get rid of the newline that Python adds after each **print**.

~~~python
print("Hello", ned='')
print("World") # Prints 'HelloWorld'
~~~

## Length and replace

**len( )**

You can get the number of characters in a string. Keep in mind it also counts the whispaces

~~~python
s = "12a"
print(len(s)) #Prints '3'
~~~

**replace( )**

Replace a specified word with another one. Keep in mind this is case sensitive.

~~~
s = "This country is the best"
print(s.replace('country', 'world')) # Prints 'This world is the best'
~~~

### Other useful methods

~~~python
# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())
~~~
