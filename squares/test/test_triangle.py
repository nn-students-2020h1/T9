import unittest
from squares.triangle import Triangle


class TestFigureSquares(unittest.TestCase):
    def setUp(self):
        self.triangle = Triangle(0, 0)

    def tearDown(self):
        self.triangle.h = 0
        self.triangle.a = 0

    def test_square_int(self):
        triangle = Triangle(1, 2)
        self.assertEqual(triangle.square(), 1)

    def test_square_negative(self):
        triangle = Triangle(-1, -2)
        with self.assertRaises(ValueError):
            triangle.square()

    def test_square_zero(self):
        triangle = Triangle(0, 0)
        self.assertEqual(triangle.square(), 0)

    def test_square_float(self):
        triangle = Triangle(1.2, 1.2)
        self.assertEqual(triangle.square(), 1.2 * 1.2 / 2)

    def test_square_dict(self):
        triangle = Triangle([1], [2])
        with self.assertRaises(TypeError):
            triangle.square()

    def test_square_bool(self):
        triangle=Triangle(False, True)
        with self.assertRaises(TypeError):
            triangle.square()

if __name__ == '__main__':
    unittest.main()
