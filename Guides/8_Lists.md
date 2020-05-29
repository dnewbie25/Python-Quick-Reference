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

