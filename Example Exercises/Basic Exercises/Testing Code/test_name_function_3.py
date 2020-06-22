# We'll create a Passing Test

import unittest
from names_function_1 import get_formatted_name

class NameTestCase(unittest.TestCase): # We create a class that inherits from unittest.TestCase
  """Test for 'names_functions_1.py'."""

  def test_first_last_name(self):
    """Do names like 'Janis Joplin' work?"""

    formatted_name = get_formatted_name('janis', 'joplin', 'maria')
    self.assertEqual(formatted_name, 'Janis Maria Joplin')

if __name__ == '__main__':
  unittest.main()