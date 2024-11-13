import unittest
from unittest.mock import patch
from calculate import calc

class TestCalculate(unittest.TestCase):

    # Тесты для корректных вычислений

    def test_circle_area(self):
        with patch('builtins.print') as mocked_print:
            result = calc('circle', 'area', [5])
            self.assertAlmostEqual(result, 78.53981633974483)
            mocked_print.assert_called_with('Area of circle with size(s) [5] is 78.53981633974483')

    def test_circle_perimeter(self):
        with patch('builtins.print') as mocked_print:
            result = calc('circle', 'perimeter', [5])
            self.assertAlmostEqual(result, 31.41592653589793)
            mocked_print.assert_called_with('Perimeter of circle with size(s) [5] is 31.41592653589793')

    def test_square_area(self):
        with patch('builtins.print') as mocked_print:
            result = calc('square', 'area', [4])
            self.assertEqual(result, 16)
            mocked_print.assert_called_with('Area of square with size(s) [4] is 16')

    def test_square_perimeter(self):
        with patch('builtins.print') as mocked_print:
            result = calc('square', 'perimeter', [4])
            self.assertEqual(result, 16)
            mocked_print.assert_called_with('Perimeter of square with size(s) [4] is 16')

    def test_triangle_area(self):
        with patch('builtins.print') as mocked_print:
            result = calc('triangle', 'area', [3, 4, 5])
            self.assertAlmostEqual(result, 6.0)
            mocked_print.assert_called_with('Area of triangle with size(s) [3, 4, 5] is 6.0')

    def test_triangle_perimeter(self):
        with patch('builtins.print') as mocked_print:
            result = calc('triangle', 'perimeter', [3, 4, 5])
            self.assertEqual(result, 12)
            mocked_print.assert_called_with('Perimeter of triangle with size(s) [3, 4, 5] is 12')

    # Тесты для обработки ошибок

    def test_invalid_figure(self):
        with self.assertRaises(ValueError) as context:
            calc('tetrahedron', 'area', [5])
        self.assertIn("Figure'tetrahedron' is not available. Available figures: ['circle', 'square', 'triangle']", str(context.exception))

    def test_invalid_function(self):
        with self.assertRaises(ValueError) as context:
            calc('circle', 'speed', [5])
        self.assertIn("Function 'speed' is not available. Available functions: ['area', 'perimeter']", str(context.exception))

    def test_negative_size_circle(self):
        with self.assertRaises(ValueError) as context:
            calc('circle', 'area', [-5])
        self.assertIn("Radius of square must be positive.", str(context.exception))

    def test_negative_size_square(self):
        with self.assertRaises(ValueError) as context:
            calc('square', 'area', [-4])
        self.assertIn("Value of square sides can not be below 0", str(context.exception))

    def test_negative_size_triangle(self):
        with self.assertRaises(ValueError) as context:
            calc('triangle', 'area', [3, -4, 5])
        self.assertIn("Value of triangle sides can not be below 0", str(context.exception))

    def test_triangle_inequality(self):
        with self.assertRaises(ValueError) as context:
            calc('triangle', 'area', [1, 2, 10])
        self.assertIn("Value of this sides can not make triangle", str(context.exception))

    def test_incorrect_parameter_count_circle(self):
        with self.assertRaises(ValueError) as context:
            calc('circle', 'area', [3, 4])
        self.assertIn("For the figure 'circle' 1  parameters are required , but was provided 2", str(context.exception))

    def test_incorrect_parameter_count_triangle(self):
        with self.assertRaises(ValueError) as context:
            calc('triangle', 'area', [3, 4])
        self.assertIn("For the figure 'triangle' 3  parameters are required , but was provided 2", str(context.exception))


if __name__ == "__main__":
    unittest.main()
