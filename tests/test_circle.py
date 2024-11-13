import unittest
from circle import area, perimeter
import math


class TestCircle(unittest.TestCase):

    def test_area_positive_radius(self):
        radius = 3
        expected_area = math.pi * radius * radius
        self.assertAlmostEqual(area(radius), expected_area)

    def test_area_zero_radius(self):
        radius = 0
        expected_area = 0
        self.assertEqual(area(radius), expected_area)

    def test_area_negative_radius(self):
        radius = -3
        with self.assertRaises(ValueError):
            area(radius)

    def test_perimeter_positive_radius(self):
        radius = 3
        expected_perimeter = 2 * math.pi * radius
        self.assertAlmostEqual(perimeter(radius), expected_perimeter)

    def test_perimeter_zero_radius(self):
        radius = 0
        expected_perimeter = 0
        self.assertEqual(perimeter(radius), expected_perimeter)

    def test_perimeter_negative_radius(self):
        radius = -3
        with self.assertRaises(ValueError):
            perimeter(radius)


if __name__ == '__main__':
    unittest.main()
