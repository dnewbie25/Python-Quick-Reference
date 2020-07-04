from random import choice

class RandomWalk:

  """A class that generates random walks"""
  def __init__(self, num_points=5000):

    """Initialize the attributes of a walk"""
    self.num_points = num_points # the numbers of points in the walk, it can be as many as you want

    # All walks start at (0, 0)
    self.x_value = [0]
    self.y_value = [0]

  def fill_walk(self):
    """Calculate all the points in the walk"""

    while len(self.x_value) < self.num_points: # it will create 5000 points before stopping
    # Decide where to go and how far to go in that direction
      x_direction = choice([1, -1]) # go right of left
      x_distance = choice([1, 2, 3, 4, 5]) # how many points it will move
      x_step = x_direction * x_distance # to get a positive or negative value of the distance so it can be 1 to 5 points right or left

    # Decide where to go vertical
      y_direction = choice([1, -1])
      y_distance = choice([1, 2, 3, 4, 5])
      y_step = y_direction*y_distance

    # If x or y are 0 just ignore the 0 point 

      if x_step == 0 and y_step == 0:
        continue

    # Calculate the resulting point

      x = self.x_value[-1] + x_step # remember that we are appending an array so new values will be always the last ones [-1]
      y = self.y_value[-1] + y_step

      self.x_value.append(x)
      self.y_value.append(y)