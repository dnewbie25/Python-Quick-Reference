# Files And Exceptions

One of the most desired features when using a program is the ability to use previous stored data no matter if it's inside our program or from an external file. The ability to load data and not having to star from scratch every time we close a file is what defines modern applications.

Also, you don't want you program to crash every time it encounters a bad input from user, if this happened Facebook would not work. You would have to reload the page every time you enter a wrong email or password.

Python allows you to handle unexpected situations like this (they are more common than you think) where users put incorrect data.

Let's start with the basics, reading different types of files:

## Reading A File

For this example, you will create a **.txt** file inside your working directoy. Once you create it put the Pi digits, at least 15 of them, 3.14159265358979.

Save it as **pi_digist.txt** and try to open it with Python as follows:

~~~python
with open('pi_digist.txt') as file_object: # Tells Python to look for that file and assigns it to 'file_object'. This is like the Aliases when you name a module in a different way
  contents = file_object.read()
  
print(contents.rstrip()) # Prints '3.14159265358979'. Remember that rstrip( ) removes whitespaces at the right of the program...this includes new lines
~~~

**with**: This one tell Python to open a program and close it once the task is completed. This is useful because if you **open( )** a file and doesn't **close( )** it correctly you will end up with corrupted data or if you close it too early you will end up working with a close program, hence all your won't save. With **with** Python will take care of that for you closing the program once the block of code finishes.

**open( )**: This statement tells Python to open the specified file.

**read( )**: This method is self explanatory, you read the file.Keep in mind this method returns an empty string at the end of the string. To delete it you can use rstrip( ) to delete the blank line after the data.

#### File Paths

It could be easy for you to pass the wrong file location. Make sure you enter slashes and not backslashes in the paths, for example 'C:\User\Documents\pi_digits.txt' will cause an error. Backslashes are used just for escaping characters. You must use slashes instead, like this 'C:/User/Documents/pi_digits.txt'.

## Reading Line By Line

If we want to know what is in every line of the text file we can do the following. Modify the *.txt* file so you have this three lines:
*3.1415926535*
 *8979323846*
 *2643383279*
 
Save the file and go back to our Python program and loop through each line:

~~~python
with open('pi_digits') as filename:
  for line in filename:
    print(line) 
'''The previous code will print:
3.1415926535

 8979323846
 
 2643383279
 
'''
#If we want to remove the whitespaces we have to delete every whitespace at the right using rstrip( )
with open('pi_digits') as filename:
  for line in filename:
    print(line.rstrip()) 
 '''Prints:
 3.1415926535
 8979323846
 2643383279'''
~~~

## Making A List Of Lines

With the **with** instruction you can only work with files inside the code block. If you want to work with the lines of a file somewhere else in your code that's outside the **with** block you can store them in a list:

Let's say we are saving the *.txt* file the same way, the pi digits split among three lines.

~~~python
filename = 'pi_digits.txt' # We store the file in a variable...yup, variable can contain complete documents.

with open(filename) as file_object: # We create a file_object Alias to refer to 'filename'
  lines = file_object.readlines() # readlines() stores the file lines in a list...do not confuse with readline()
  
for line in lines:
  print(line.rstrip()) # Prints each line stored in the list
~~~

Our code has a **readlines( )** method. This one stores each line as an element in a list, ['3.1415926535\n', ' 8979323846\n', ' 2643383279'] with a *\n* escape character at the end. Now, do not think it's the same as **readline( )**, one is plural and the other is singular. This last one **reads only the first line of the file**.

## Working With A File's Contents

Once you read a file you can do a lot of different stuff with it. Let's try to print the pi digits in one line without using any special method, just a loop.

There are a lot of way to work with external files. You can read the code directly here so you can figure out what's happening. Reading other people's code is a must in order to learn programming.

- [Reading Files Basics](https://github.com/dnewbie25/Python-Quick-Reference/blob/master/Example%20Exercises/Basic%20Exercises/26_Reading_Files.py)

- [Reading Files Exercises](https://github.com/dnewbie25/Python-Quick-Reference/blob/master/Example%20Exercises/Basic%20Exercises/27_Reading_Files_Exercises.py)

## Storing Data

To store data you can just se the **JSON module**. Thi format was created initially for Javascript but it has become a standard in the industry since then, even for Python and other bunch of programming languages.

As every other module, you need to import it before using it:

~~~python
import json
~~~

Once you import it you can start using its functions.

### json.dump( )

This function is used to store information in a data structure (lists, tuples, dictionaries). It needs two arguments, first it needs the piece of data it will store and second the file object where you want to store that data:

~~~python
import json

numbers = [1,2,3,4,5,6,7]

filename = 'numbers.json' # You create a file .json

with open(filename, 'w') as file_object: # Open the file in write mode
  json.dump(numbers, file_object) # Call the json.dump() and pass the list because you want to save it and the file_object, which is the alias for the filename
  
# Now the numbers list should be stored in the json file if you open it
~~~

### json.load( )

If we want to read the data we store in a json file we can simply use this function as follows:

~~~python
import json

filename = 'numbers.json'

with open(filename) as file_to_read: # This one reads the file
  numbers_to_display = json.load(file_to_read) # Loads the data into the numbers_to_display
  
print(numbers_to_display) # Displays the loaded data
~~~

## Saving And Using User-Generated Data

When you use a program you want to store information on it, whther it's your data of the user's data. JSON files are very useful here:

~~~python
import json

username = input("Enter you user name: ")

filename = 'usernames.json'

with open(filename, 'w') as f:
  json.dump(username, f)
  print(f"We'll remember when you come back, {username}")
~~~

If you want to read the user name just use the same **json.load( )** function we use previously.

~~~python
import json

filename = 'usernames.json'

with open(filename) as f:
  username = json.load(f)
  print(f"Hello, {username}, how are you?")
~~~

Now, as in real-world programs you need to store and load data in the same program. You don't want to open individual files every time you need to load some data. You don't want unexpected crashes because the username was not found so we'll rely on some not so old friends, **try-except**.

~~~python
import json

filename = 'usernames.json'

try:
  with open(filename) as f: # You will try to read the file first. If it is not possible then you'll create a new entry for that file
    username = json.load(f)
except FileNotFoundError: # If the file doesn't exist then you will create a username
  username = input("What is your username?: ")
  with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember your username: {username}")
else: # If the try was successful and the file exists it will print this message
  print(f"Welcome back, {username}!!")
~~~
