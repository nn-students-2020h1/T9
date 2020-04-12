import unittest
from squares.squares import Squares
import math


class TestFigureSquares(unittest.TestCase):

    def test_square_int(self):
        self.assertEqual(Squares.square_round(self, 1), math.pi)
        self.assertEqual(Squares.square_rectangle(self, 1, 1), 1)
        self.assertEqual(Squares.square_triangle(self, 1, 2), 1)

    def test_square_negative(self):
        self.assertRaises(ValueError, Squares.square_round, self, -1)
        self.assertRaises(ValueError, Squares.square_rectangle, self, -2, -2)
        self.assertRaises(ValueError, Squares.square_rectangle, self, -2, 1)
        self.assertRaises(ValueError, Squares.square_triangle, self, -1, 1)

    def test_square_zero(self):
        self.assertEqual(Squares.square_rectangle(self, 0, 0), 0)
        self.assertEqual(Squares.square_triangle(self, 0, 0), 0)
        self.assertEqual(Squares.square_round(self, 0), 0)

    def test_square_float(self):
        self.assertEqual(Squares.square_rectangle(self, 1.2, 1.2), 1.2 * 1.2)
        self.assertEqual(Squares.square_round(self, 1.2), 1.2 ** 2 * math.pi)
        self.assertEqual(Squares.square_triangle(self, 1.2, 1.2), 1.2 * 1.2 / 2)

    def test_square_dict(self):
        self.assertRaises(TypeError, Squares.square_rectangle, self, [1, 2])
        self.assertRaises(TypeError, Squares.square_triangle, self, [1], [1])
        self.assertRaises(TypeError, Squares.square_round, self, [1])

    def test_square_bool(self):
        self.assertRaises(TypeError, Squares.square_triangle, self,  False, True)
        self.assertRaises(TypeError, Squares.square_round, self, False)
        self.assertRaises(TypeError, Squares.square_rectangle, self, False, True)

if __name__ == '__main__':
    unittest.main()
