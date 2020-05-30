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

#### sort( ) and sorted( ) - Mutable and unmutable methods

The are some methods that modify the original element, *mutable methods*, and some that doesn't, *unmutable methods*.

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
