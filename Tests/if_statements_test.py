import unittest
from even_odd import even_or_odd
from bonus import bonus
from abs_value import convert


class MyTestCase(unittest.TestCase):
    def test_even_odd(self):
        self.assertEqual("13 is an odd number", even_or_odd(13))
        self.assertEqual("24 is an even number", even_or_odd(24))

    # In the space below, write a test function for bonus. Make sure to import the appropriate information
    # at the top of this file. Make sure to write three test cases.
    def test_bonus(self):
        self.assertEqual("Your total salary is: 5.25", bonus(5, 6))
        self.assertEqual("Your total salary is: 5", bonus(5, 5))

    def test_abs(self):
        self.assertEqual("The absolute value of -5.0 is 5.0", convert(-5))
        self.assertEqual("The absolute value of 5.0 is 5.0", convert(5))
        self.assertEqual("The absolute value of 0.0 is 0.0", convert(0))

if __name__ == '__main__':
    unittest.main()
