# Lists or Arrays

This chapter will be long enough to count as two or three sections. Lists, as wee as dictionaries and tuples are other kinds of data types you'll use almost all the time. Once you finish this section you can start writing a vast number of programs. Variables, strings, numbers, functions, loops, conditionals and lists. These are the foundations of every programming language

Now for short, a list is a way to store multiple elements in one single variable and being able to access them by using indexes. Think of it as a bookshelf, with every book labeled as the first, second or third one in the bookshelf. **It's a collection of items in a particular oder**.

You can put anything you want in the order you want

~~~python
bicycles = ['trek', 'cannondale', 'redline', 'specialized'] # Each element must be separated by a comma
print(bicycles) # Prints ['trek', 'cannondale', 'redline', 'specialized']
~~~

You can access elements in a list by using its index[ ]. Remember that a computer starts counting in zero.

~~~python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0]) # Prints 'trek'
print(bicycles[3].upper()) # Prints 'SPECIALIZED'
~~~

## Changing, Adding or Removing Elements

### Changing elements

You can modify an element in a list by using the **index[ ]** as if you were accessing it.

~~~python
motorcylces = ['honda', 'yamaha', 'ducati']
motorcyles[1] = 'bmw'
print(motorcyles) # Prints ['honda, 'bmw', 'ducati']
~~~

### Adding elements

Theres are many ways to add elements to an existing list, no mattre if it has 0 elements or 100,000 elements.

#### append( ) - Adds at the END of the list

The easiest way to add an element:

~~~python
motorcylces = ['honda', 'yamaha', 'ducati']
motorcycles.append('ktm')
print(motorcycles) # Prints ['honda', 'yamaha', 'ducati', 'ktm']
~~~

Or you cna just create an empty list and add elements to it:

~~~python
motorcycles = [] # Creates an empty list

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles) # Prints ['honda', 'yamaha', 'suzuki']
~~~

#### insert( ) - Inserting elements into a list

With this method you can add an element at any position within a list. It does not remove the previous item in that position, it just move it to the next index. You have to specify the index and the value you want to add:

~~~python
motorcylces = ['honda', 'yamaha', 'ducati']
motorcycles.insert(1, 'panigale') # Inserts 'panigale' at index 1

print(motorcycles) # Prints ['honda', 'panigale', 'yamaha', 'ducati'] # 'yamaha' is then moved to index 2
~~~

### Removing elements

Often you might want to remove an item or a set of items in a list.

#### del Statement

If you know the position of the item you use **del** to delete the item at that index:

~~~python
motorcycles = ['honda', 'yamaha', 'ducati']

del motorcycles[2] # Deletes 'ducati'

print(motorcycles) # prints['honda', 'yamaha']
~~~

#### pop( ) - Deletes at the END of the list

The **pop( )** method will remove any element at the end of a list, no matter how big your list is, but, and this is the great part about pop( ), it will let you work with the removed item because this functions returns the item you just deleted.

Let's say we want to remove the last element 'bmw' and add it to a new list of high-end motorcycles:

~~~python
motorcyckles = ['honda', 'yamaha', 'suzuki', 'bmw']
high_end_motorcycles = [] # An empty list

high_end_motorcycles.append(numbers.pop()) # Yes! You can combine functions. You can create a new variable to store the pop() return, but we just wanted to make it quicker

print(motorcycles) # Prints ['honda', 'yamaha', 'suzuki']
print(high_end_motorcycles) # Prints ['bmw']
~~~

**pop( ) can be used to delete any item in the list too** by using the index inside the paranthesis:

~~~python
motorcycles = ['honda', 'yamaha', 'suzuki', 'bmw']
motorcycles.pop(2) # Removes 'suzuki'

print(motorcycles) # Prints ['honda', 'yamaha', 'bmw']
~~~

**How to choose between *del* and *pop( )*?** 

Simple. If you want to use the deleted item, use **pop( )**. but if you want to remove the item forever and don't want to use later in any way, use **del**.

#### remove( ) - Deletes an item by its value

Many time syou won't know the index of a value, but it's really rare not to know the value or string you want to delete, so here comes **remove( )** to save your life.

~~~python 
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 

motorcycles.remove('yamaha')
print(motorcycles) # Prints ['honda', 'suzuki', 'ducati'] 
~~~

You can even use **remove( )** to use the item to delete:

~~~python
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 

high_end_moto = 'ducati'
motorcycles.remove(high_end_moto)
print(f"{high_end_moto} is too expensive for me, maybe I could buy one of these:{motorcycles}") # Prints 'ducati is too expensive for me, maybe I could buy oe of these:['honda', 'yamaha', 'suzuki']'
~~~

**NOTE:** The remove( ) method deletes just the first element it encounters with that value. If the element appears more than one time you might need to create a loop to get rid of all of its occurences.

## Organizing A List

As with any set of elements, we can present it unordered, which is not very professional, or ordered in numerical or alphabetical order. For our sake, Python implements a couple of methods to sort lists which can be really handful.

#### sort( ) and sorted( ) - Mutable and immutable methods

The are some methods that modify the original element, *mutable methods*, and some that doesn't, *immutable methods*.

**sort( )** is a mutable one. It modifies the original list forever when sorts it.

~~~python
colors = ['red', 'blue', 'green', 'yellow']
colors.sort()
print(colors) # Prints ['blue', 'green', 'red', 'yellow'] 
~~~

**sorted( )**, on the other hand, does not modify the original item forever. Note that in *sorted( )* the list must be called inside the parenthesis.

~~~python
colors = ['red', 'blue', 'green', 'yellow']
print(colors) # Prints ['red', 'blue', 'green', 'yellow']

print(sorted(colors)) # Prints ['blue', 'green', 'red', 'yellow'] --> As you can see it sorts the list but doesn't change the original one

print(colors) # Prints ['red', 'blue', 'green', 'yellow'], the original list
~~~

#### (reverse = True) and reverse( ) - Sort in Reverse Order

If you want to sort backwards in numerical of alphabetical order, from the greater value to the lowest one, or from 'Z' to 'A' you must add **reverse = True** inside the **sort( )** methods.

~~~python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars) # Prints ['toyota', 'subaru', 'bmw', 'audi'] 
~~~

You can even use the **reverse = True** inside the **sorted( )** method if you don't want to change the original list order.

~~~python
colors = ['red', 'blue', 'green', 'yellow']
print(colors) # Prints ['red', 'blue', 'green', 'yellow']

print(sorted(colors, reverse = True)) # Prints ['yellow', 'red', 'green', 'blue'] --> As you can see it sorts the list but doesn't change the original one

print(colors) # Prints ['red', 'blue', 'green', 'yellow']
~~~

But, on the other hand, if you want to order from last index to first index, you have to use **reverse( )**. This one modifies the original list (mutable method) with the last element as the first one, the second last element as the second one and so on.

~~~python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars) # Prints ['bmw', 'audi', 'toyota', 'subaru']

cars.reverse() # Reverse the list from last index to first one
print(cars) # Prints ['subaru', 'toyota', 'audi', 'bmw'] # As you can see, they are not in alphabetical order. It literally reversed the list
~~~

## Finding The Length Of A List

If you want to know the length of a list, you just need to use the same method you use for the length of a string, **len( )**. This method will count as humans do, starting with 1.

~~~python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars)) # Prints 4
~~~

## Avoiding Index Error

If you played a bit with indexes you might have found that when you try to access an index that does not exist you get a *IndexError* in the console. You can handle this kind of issues in order to not crashing your program in a similar you saw in the *Functions* chapter.

~~~python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[3])
~~~

Te previous code will return:

~~~python
Traceback (most recent call last):
 File "motorcycles.py", line 2, in <module>
 print(motorcycles[3])
IndexError: list index out of range # This is the name of the error
~~~

Remember that computers start counting at zero but whe start at 1. SO if your list has 3 elements, the last index would be two, because for a computer the indexes are 0, 1 and 2.

If you need the last item of a list but don't remember how many items it has, you can search with **negative numbers** like **-1**. This way the interpreter will search from the first item at the end of the list:

~~~python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[-1]) # This will print 'suzuki'
print(motorcycles[-3]) # This will print 'honda'
~~~

See that in this case the first item, when counting in negative numbers, has the value of -3. Remember that negative numbers don't include the zero, and the computer will start from -1.

If you find issues when working with the indexes in a list, it's really helpful to print the **length of the list** to see if you are working with the right number of indexes.

## Looping Through A List

**for** is the loop you want to use with lists, because it allows you to go through each element in the list without major issues:

~~~python
my_pets = ['cat', 'dog', 'parrot', 'snake']

for pet in my_pets: # This creates a variable 'pet' to save the value at the specified index the loop is evaluating
 print("I have a " + pet) # This uses the 'pet' vairable to print the name of the pet at that index
~~~

## Numerical Lists

Lists can be very useful when working with numerical values, so as in the **loop** section, the **range( )** function can be use to count elements in a list. Remember this range( ) function is inclusive-exclusive, [x, y).

~~~python
my_pets = ['cat', 'dog', 'parrot', 'snake', 'horse', 'monkey', 'hamster']

for favorite in range(1,5): # This one loops from index one through index 4, and stops when reaches index 5.
 print("My favorite pet is " + favorite) # Prints from 'dog' to 'horse' --> [1, 5)
~~~

#### Creating Numerical Lists

You can create numerical lists easily using the **range( )** function too and the **list( )** function.

~~~python
my_range = list(range(1,11))
prints(my_range) # Prints [1,2,3,4,5,6,7,8,9,10], remember [1, 11)
~~~

As with the *range( )* used in the loops, you can modify the increment value by passing a third parameter. For example, let's create a list from 1 to 10 that prints just the even numbers:

~~~python
evens = list(range(2, 11, 2)) # Starts at 2 inclusive until 11 exclusive, [2, 11), and increases by 2 every following item
print(evens) # Prints [2,4,6,8,10]
~~~

#### min, max and sum

You can find the minimun, maximun and the sum of all the numerical elements in a list:

~~~python
numbers = [1,2,3,4,5,6,7,8,9,10]
print(min(numbers)) # Prints 0
print(max(numbers)) # Prints 10
print(sum(numbers)) # Prints 55
~~~

## List Comprehensions

There's a concept that simplyfies the way you create lists. For exampe, if you want to create a list which contains all the squares from 1 to 10, you can¿t use the **list( )** instruction. You would need to use a **for** loop:

~~~python
squares = []

for number in range(1,11): # Creates a simple for loop from 1 to 10 inclusive
 squares.append(number**2) # Appends each numbers's square
 
print(squares) # Prints [1,4,9,16,25,36,49,64,81,100]
~~~

But, imagine that the list you want to create has a lot of lines in a for loop. We can just create the list in a simpler way. For example, if we want to create the same list for suqares, we could use **list comprehension** to do so:

~~~python
squares = [number**2 for number in range(1,11)]  # It defines that each number will be squared in a range from [1,11)
print(squares) # Prints [1,4,9,16,25,36,49,64,81,100]
~~~

## Slice

If you want to use just a part of the list you can slice it by specifying the **[start : end]** of the slice, with that syntax. This works inclusive-exclusive, like the **range( )** method.

~~~python
players = ['charles', 'martina', 'michael', 'florence', 'eli'] 

print(players[0:4]) # Prints ['charles','martina', 'michael', 'florence']

print(players[:4]) # When ou don't put a zero Python assumes you meant [0:whatever_value]
~~~

You can also set the start of the slice with no end, **[start : ]**:

~~~python
players = ['charles', 'martina', 'michael', 'florence', 'eli', 'dani', 'lorenzo', 'victor', 'rachel'] 

print(players[3:]) # Prints ['florence', 'eli', 'dani', 'lorenzo', 'victor', 'rachel']
~~~

**You can slice with negative numbers** too. It does not print backwards. It prints the last *n* elements but in the same order they appear in the original list.

~~~python
players = ['charles', 'martina', 'michael', 'florence', 'eli', 'dani', 'lorenzo', 'victor', 'rachel'] 

print(players[-5:]) # Prints ['eli', 'dani', 'lorenzo', 'victor', 'rachel'] 
~~~

#### Loop A Slice

You can loop a slice as if it were the range of the **for** loop:

~~~python
players = ['charles', 'martina', 'michael', 'florence', 'eli', 'dani', 'lorenzo', 'victor', 'rachel'] 

for winner in  players[:3]:
 print("You classify to the next round, " + winner) # This will print the text starting with 'charles' and finishing with 'michael', [0:3)
~~~

## Copying A List

If you want to create a list, you might think about using *copy_list = my_list*, but this will make both variables point to the same list. If you want to copy a list in order to work separately from the original one, you must use **[ : ]**:

~~~python
# If you modify my_foods_1, then you will be modifying friends_food_1 at the smate time

my_foods_1 = ['pizza', 'falafel', 'carrot cake']
friends_foods_1 = my_foods_1

my_foods_1.append('cannoli')
friends_foods_1.append('ice cream')

print("My favorite foods are:")
print(my_foods_1)  # Prints ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
print("\nMy friend's favorite foods are:")
print(friends_foods_1) # Prints ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']

# But if you use [ : ] then you could use each list independently

my_foods_2 = ['pizza', 'falafel', 'carrot cake']
friends_foods_2 = my_foods_2[:]

my_foods_2.append('cannoli')
friends_foods_2.append('ice cream')

print("My favorite foods are:")
print(my_foods_2)  # Prints ['pizza', 'falafel', 'carrot cake', 'cannoli']
print("\nMy friend's favorite foods are:")
print(friends_foods_2) # Prints ['pizza', 'falafel', 'carrot cake', 'ice cream']
~~~
