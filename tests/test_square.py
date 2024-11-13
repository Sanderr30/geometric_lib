import unittest
from square import area, perimeter


class TestSquare(unittest.TestCase):

    def test_area_valid_square(self):
        side_length = 5
        expected_area = side_length * side_length
        self.assertEqual(area(side_length), expected_area)

    def test_area_negative_side(self):
        side_length = -5
        with self.assertRaises(ValueError):
            area(side_length)

    def test_perimeter_valid_square(self):
        side_length = 5
        expected_perimeter = 4 * side_length
        self.assertEqual(perimeter(side_length), expected_perimeter)

    def test_perimeter_negative_side(self):
        side_length = -5
        with self.assertRaises(ValueError):
            perimeter(side_length)


if __name__ == '__main__':
    unittest.main()
