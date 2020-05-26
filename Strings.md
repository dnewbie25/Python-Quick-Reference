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






