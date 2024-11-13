import unittest
from square import area, perimeter

class TestSquare(unittest.TestCase):
    def test_area_valid_square(self):
        side = 5
        expected_area = side * side
        self.assertEqual(area(side), expected_area)

    def test_area_negative_side(self):
        side = -5
        with self.assertRaises(ValueError):
            area(side)

    def test_perimeter_valid_square(self):
        side = 5
        expected_perimeter = 4 * side
        self.assertEqual(perimeter(side), expected_perimeter)

    def test_perimeter_negative_side(self):
        side = -5
        with self.assertRaises(ValueError):
            perimeter(side)

if __name__ == '__main__':
    unittest.main()
