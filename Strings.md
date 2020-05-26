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







