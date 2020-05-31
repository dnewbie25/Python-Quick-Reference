numbers = [33,25,12,41,58,78,95,65,21,10,11,2,5,4,1]

# Slice first 3 

print("The first 3 items are :" + str(numbers[0:3]))

print("Three items from the middel of the list :" + str(numbers[6:10]))

print("The last three items are :" + str(numbers[-3:]))

# My Pizzas, You Pizzas

pizzas = ['Napolitan', 'Margaritta', 'Hawaian']

friends_pizzas = pizzas[:]

friends_pizzas.append('Chicken BBQ')
pizzas.append('Jalapeño')

print(f"My favorite pizzas are : {pizzas}")

print(f"My friend's favorite pizzas are : {friends_pizzas}")

# For loop over a slice
i = 1
for value in numbers[0:10]:
  
  print(f"The item #{i} in my list is {value}")
  i+=1