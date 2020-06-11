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
