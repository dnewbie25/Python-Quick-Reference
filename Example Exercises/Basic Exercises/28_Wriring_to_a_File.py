# If you want to write in a file you need to use a second argument in open( )

filename = 'Files Samples/programming.txt' # If you declare the path you don't need to create the file. Python will create it automatically

with open(filename, 'w') as file_object: # the 'w' means 'writing'
  file_object.write("I love to program")

'''
There are three modes to open a file in Python, read ('r') --> the default mode, write ('w') and append ('a')

And a third mode to read and write at the same time ('r+') 
'''

# 'w' mut not be used with a file that already exists because it will erase the preivous data it had

print("\n\n----------Wiring Multiple Lines-----------\n\n")

filename2 = 'Files Samples/multiple_lines.txt'

with open(filename2, 'w') as file_object_2:
  file_object_2.write("Hi this is my 1st line\n")
  file_object_2.write("And this is my second one jeje")
  

print("\n\n----------Appending to a File-----------\n\n") # If you want to add content onstead of erasing and writing over the existing file


filename3 = 'Files Samples/multiple_lines.txt' # This file already exists

with open(filename3, 'a') as file_object_3:
  file_object_3.write("\n\nThis is the line I appended :v\n") # The append mode uses the write() method



