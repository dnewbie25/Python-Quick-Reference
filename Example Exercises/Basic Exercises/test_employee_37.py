import unittest
from Testing_Exercise_37 import Employee

class TestEmployee(unittest.TestCase):
  """Test the Employee raise amount"""
  
  def setUp(self):
    """Create an instance of Employee to test"""
    self.test_employee = Employee('Dani', 'Montoya', 25000)

  def test_give_default(self):
    """Tets the default value of raiseAmount, which is 5000"""
    self.assertEqual(self.test_employee.give_raise(), 30000)

  def test_give_custom_raise(self):
    """Test the raiseAmount when specified by the user"""
    self.assertEqual(self.test_employee.give_raise(10000), 35000)

if __name__ == '__main__':
  unittest.main()
