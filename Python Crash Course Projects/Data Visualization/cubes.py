import matplotlib.pyplot as plt

number = []

for item1 in range(1, 5001):
  number.append(item1)

cubes = []

for item2 in number:
  cubes.append(item2**3)

plt.style.use('ggplot') # assigns that style

fig, ax = plt.subplots() # creates a figure containing a single axes

ax.scatter(number, cubes, c = cubes, cmap = plt.cm.YlOrRd, s = 7) # adds the data to the axes created before

plt.show()