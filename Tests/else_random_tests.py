import unittest
from divisible import is_divisible
from exams import gets_a_zero
from maximum import max

class MyTestCase(unittest.TestCase):
    def test_maximum(self):
        self.assertEqual(2, max(2, 1))
        self.assertEqual(3, max(2, 3))
        self.assertEqual(4, max(-1, 4))
        self.assertEqual(-1, max(-1, -2))
        self.assertEqual("The numbers are equal", max(1, 1))

    def test_is_divisible(self):
        self.assertTrue(is_divisible(6, 3))
        self.assertFalse(is_divisible(19, 5))
        self.assertFalse(is_divisible(3, 6))
        self.assertTrue(is_divisible(5, 5))
    def test_exams(self):
        self.assertTrue(gets_a_zero(25, 10))
        self.assertTrue(gets_a_zero(32, 8))
        self.assertFalse(gets_a_zero(20, 0))
        self.assertFalse(gets_a_zero(32, 7))

if __name__ == '__main__':
    unittest.main()
