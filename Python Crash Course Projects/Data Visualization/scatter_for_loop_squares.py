import matplotlib.pyplot as plt 

x_values = range(1, 1001) # remember range is inclusive-exclusive
y_values = [x**2 for x in x_values] # this is  alist comprehension

plt.style.use('seaborn') # the style of our graph

fig, ax = plt.subplots()

ax.scatter(x_values, y_values, s=15)

# chart and label axes title

ax.set_title("1000 first squares", fontsize = 15)

ax.set_xlabel("Value", fontsize = 14)

ax.set_ylabel("Square of Value", fontsize = 14)

# set the range for each axis
ax.tick_params(axis = 'both', which='major', labelsize = 7)


ax.axis([0, 1100, 0, 11000000])

plt.show()