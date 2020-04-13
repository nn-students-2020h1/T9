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

    def test_square_exist(self):
        triangle = Triangle(1, 1)
        self.assertTrue(triangle.square())

    def test_is_square(self):
        triangle = Triangle(1, 2)
        square = 1
        self.assertTrue(square, triangle.square())

    def test_triangle_data(self):
        triangle = Triangle(1, 2)
        self.assertIn(triangle.h, [1, 2, 3])

    def test_traingle_None(self):
        triangle = Triangle(1, 2)
        self.assertIsNotNone(triangle)

    def test_square_is_float(self):
        triangle = Triangle(5, 10)
        self.assertIsInstance(triangle.square(), float)

    def test_warns(self):
        with self.assertWarns(Warning):
            self.triangle.sides()




if __name__ == '__main__':
    unittest.main()
