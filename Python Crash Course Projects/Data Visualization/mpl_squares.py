import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use('seaborn') # The style methods must be used before starting to generate the plot

fig, ax = plt.subplots()

ax.plot(x_values, y_values, linewidth = 0) # (X, Y) is the referral when using plot( ), here it will use the squares as the X values and the [2,4,6,8,10] as the Y values. linewidth is that, the width of the line in pixels

ax.scatter(x_values, y_values, s=200) # Stilishes individual point in the graph. In this case it puts a dot in the point (2, 4), the s means size = 200. If you put the variables it will apply scatter to all points defined as X and Y

# Set chart title and label axes

ax.set_title("Square Numbers", fontsize = 24) # sets a title
ax.set_xlabel("Value", fontsize = 14) # sets the label of the X axis and a fontsize
ax.set_ylabel("Square of Value", fontsize = 14) # sets the label of the Y axis and a fontsize



# Set size of tick labels
ax.tick_params(axis = 'both', labelsize = 14)
plt.show()
