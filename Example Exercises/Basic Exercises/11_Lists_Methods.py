# 1-20 numbers
for i in range(1,21):
  print(i)

print("\n\n")


# Numbers from 1 to 1,000,000

million = []

for x in range(1, 1_000_001): # You can separate 3 digits with an underscore
  million.append(x)

print("\n\n")

# Sum of million list

print(sum(million))
print("\n\n")

# Odd numbers

odds = []

for number in range(1,121,2):
  odds.append(number)

print(odds)
print("\n\n")

# 3 from 3 to 30

threes = []

for values in range(3,31,3):
  threes.append(values)

print(threes)
print("\n\n")

# Cubes

cubes = []

for values in range(1,11):
  cubes.append(values**3)

print(cubes)
print("\n\n")

# Cube Comprehension

cube_comprehension = [numbers**3 for numbers in range(1,11)]
print(cube_comprehension)
