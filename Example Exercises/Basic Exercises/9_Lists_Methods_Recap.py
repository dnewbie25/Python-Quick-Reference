# Each list methods should be used at leat once

my_list = ['Car', 'Trophies', 'Motorcycles', 'Airplanes', 'Ships', 'Toys']
print(my_list)

# Change an item

my_list[0] = 'Glasses'
print(my_list)

# Appends

my_list.append('Cellphones')
print(my_list)

# Insert

my_list.insert(1, 'Medals')
print(my_list)

# Del

del my_list[-1]
print(my_list)

# Pop

my_list.pop()
print(my_list)

# Remove

my_list.remove('Ships')
print(my_list)

# Sort and reverse=

my_list.sort(reverse=True)
print(my_list)

# Sorted and rever=

sorted(my_list, reverse=True)
print(my_list)

# Reverse

my_list.reverse()
print(my_list)

# Length

a = len(my_list)
print(a)

