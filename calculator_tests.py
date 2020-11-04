import unittest
import calculator

class CalculatorTests(unittest.TestCase):

 def test_add(self):
  res = calculator.Calculator()
  res.add(1, 99)
  self.assertEqual(res, 100)
	
 def test_subtract(self):
  res = calculator.Calculator()
  res.subtract(100, 99)
  self.assertEqual(res, 1)

 def test_multiply(self):
  res = calculator.Calculator()
  res.multiply(3, 25)
  self.assertEqual(res, 75)

 def test_divide(self):
  res = calculator.Calculator()
  res.divide(100, 5)
  self.assertEqual(res, 20)	
		
if __name__ == '__main__':
	unittest.main()
