import matplotlib.pyplot as plt 

from random_walk import RandomWalk 

# Make a RandomWalk instance in variable rw

rw = RandomWalk()

# Call RandomWalk fill_walk( ) method

rw.fill_walk()

# Plot the points in the walk

plt.style.use('classic') # classic style
fig, ax = plt.subplots() # creates a figure contaiing a single axes

ax.plot(rw.x_value, rw.y_value)
ax.scatter(rw.x_value, rw.y_value, c = rw.y_value,cmap= plt.cm.BrBG, s = 15) # put points in the rw x and y values

plt.show()