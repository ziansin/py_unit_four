import unittest

from triangles import is_triangle
from grades import points
from rock_paper_scissors import who_wins


class MyTestCase(unittest.TestCase):
    def test_is_triangle(self):
        self.assertTrue(is_triangle(7, 11, 16))
        self.assertFalse(is_triangle(20, 7, 11))
        self.assertFalse(is_triangle(4, 9, 3))
        self.assertFalse(is_triangle(9, 13, 22))

    def test_points_1(self):
        self.assertEqual(2, points(80, False))

    def test_points_2(self):
        self.assertEqual(0.2, points(64, True))

    def test_points_3(self):
        self.assertEqual(3, points(88, False))

    def test_points_4(self):
        self.assertEqual(4.2, points(100, True))

    def test_points_5(self):
        self.assertEqual(1.2, points(70, True))

    def test_points_6(self):
        self.assertEqual(2, points(85, False))


    def test_rps(self):
        self.assertEqual("You win!", who_wins(3, 2))
        self.assertEqual("You win!", who_wins(2, 1))
        self.assertEqual("You win!", who_wins(1, 3))
        self.assertEqual("It is a tie", who_wins(1, 1))
        self.assertEqual("It is a tie", who_wins(2, 2))
        self.assertEqual("It is a tie", who_wins(3, 3))
        self.assertEqual("The computer wins", who_wins(1, 2))
        self.assertEqual("The computer wins", who_wins(3, 1))
        self.assertEqual("The computer wins", who_wins(2, 3))

        # Put the rest of the rps tests below this line. There should be 9 in total.

if __name__ == '__main__':
    unittest.main()
