import unittest
from Triangle.triangle_class import Triangle


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.triangle = Triangle(0, 0, 0, 0, 0, 0)

    def tearDown(self):
        self.triangle.ax = 0
        self.triangle.ay = 0
        self.triangle.bx = 0
        self.triangle.by = 0
        self.triangle.cx = 0
        self.triangle.cy = 0

    def test_lenght_ac(self):
        triangle = Triangle(0, 0, 1, 1, 0, 2)
        self.assertEqual(triangle.lenght_ac(), 2)

    def test_lenght_ab(self):
        triangle = Triangle(0, 0, 1, 1, 0, 2)
        self.assertEqual(triangle.lenght_ab(), 1.4142135623730951)

    def test_lenght_bc(self):
        triangle = Triangle(0, 0, 1, 1, 0, 2)
        self.assertEqual(triangle.lenght_bc(), 1.4142135623730951)

    def test_square_wrong_data(self):
        triangle = Triangle('a', 0, 1, 1, 0, 2)
        with self.assertRaises(TypeError):
            triangle.square()

    def test_data_is_correct(self):
        triangle = Triangle(10, 0, 1, 1, 0, 2)
        self.assertTrue(triangle.square())

    def test_is_coordinate_add(self):
        triangle = Triangle(10, 0, 1, 1, 0, 2)
        triangle.ax = 5
        self.assertIs(triangle, Triangle)

    def test_perimeter_is_not_none(self):
        triangle = Triangle(13, 12, 15.3, 1, 12, 14)
        self.assertIsNotNone(triangle.perimeter())


if __name__ == '__main__':
    unittest.main()
