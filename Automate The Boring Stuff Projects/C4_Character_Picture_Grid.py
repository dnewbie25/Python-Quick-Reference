grid = [['.', '.', '.', '.', '.', '.'],
       ['.', 'O', 'O', '.', '.', '.'],
       ['O', 'O', 'O', 'O', '.', '.'],
       ['O', 'O', 'O', 'O', 'O', '.'],
       ['.', 'O', 'O', 'O', 'O', 'O'],
       ['O', 'O', 'O', 'O', 'O', '.'],
       ['O', 'O', 'O', 'O', '.', '.'],
       ['.', 'O', 'O', '.', '.', '.'],
       ['.', '.', '.', '.', '.', '.']]

'''The goal is to rotate the grid 45 degrees to the right, the result should be like:

..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....

 '''

for horizontal in range(len(grid[0])): # The first list is 6 items long
  for vertical in range(len(grid)): # This one has a length of 9 items
    print(grid[vertical][horizontal], end="") # Prints without creating a new line

  print() # Fater printing the line, it jumps to the next line but with no whitespace between lines

''' 

An explanation of the frist line grid[vertical][horizontal]
grid[0][0] = '.'
grid[1][0] = '.'
grid[2][0] = '0'
grid[3][0] = '0'
grid[4][0] = '.'
grid[5][0] = '0'
grid[6][0] = '0'
grid[7][0] = '.'
grid[8][0] = '.'

At every vertical it will take the index 0 of that list, and will print it horizontally as a string

'''
  
