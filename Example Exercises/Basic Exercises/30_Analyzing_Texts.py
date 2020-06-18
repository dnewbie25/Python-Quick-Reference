# Analyze Alice in Wonderlan

# If the files does not exist you will get a FileNotFoundError

filename = 'Files Samples/Aalice_Wonderland.txt'
'''
try:
  with open(filename, encoding='utf-8') as book: # The txt was downloaded as utf-8, so we need to declare the encoding in order to read all the characters correctly
    content = book.read()  
except FileNotFoundError:
  print(f"\nSorry, the file {filename} does not exist\n")
'''
# Let's count the number of words

try:
  with open(filename, encoding='utf-8') as book_to_count:
    content_2 = book_to_count.read() # In order to read the content
except FileNotFoundError:
  print(f"\nSorry, the file {filename} does not exist\n")
else: # If the try was successful then executes this line. If you don't use this and the path is incorrect it won't show a FileNotFoundError, instead it will say the content_2 was not defined

  list_words = content_2.split() # Separate each word and creates a list if the try was correct
  num_words = len(list_words)
  print(f"Alice in Wonderland has {num_words}")

####More books to analyze#######


# Create a count words functions

def count_words(filename):

  '''Count the approximate number of words in a file'''

  try:
    with open(filename, encoding='utf-8') as book:
      content = book.read()
  except FileNotFoundError:
    # print(f"The file {filename} was not found")
    '''If we want ou program to fail silently without giving error messages every time we can just use pass'''
    pass # This won't print anything to the console
  else:
    list_from_words = content.split()
    num_word = len(list_from_words)
    print(f"The number of words of {filename} is {num_word}")

filename = 'Files Samples/lice_Wonderland.txt'
count_words(filename)

# We can even create a list of file paths. The Moby Dick path has an error but the program should run until the end

filenames_list = ['Files Samples/Alice_Wonderland.txt', 'Files Samples/M--oby Dick.txt', 'Files Samples/Siddhartha.txt']

for books in filenames_list: # This executes the count_words function
  count_words(books)

