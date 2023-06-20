#!/usr/bin/python3
"""Test Square class"""
import unittest
from io import StringIO
from contextlib import redirect_stdout
from models.rectangle import Rectangle
from models.square import Square


class SquareTestCase(unittest.TestCase):
    """Defines all test cases for the Square class"""
    def test_subclass_check(self):
        self.assertTrue(issubclass(Square, Rectangle))

    def test_Square_id(self):
        s = Square(5, 0, 0, 1)
        s2 = Square(5)
        self.assertEqual(s.id, 1)
        self.assertNotEqual(s.id, s2.id)

    def test_no_params(self):
        with self.assertRaises(TypeError):
            s = Square()

    def test_x_and_y_params(self):
        s = Square(5, 0, 0, 12)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_width_and_height_params(self):
        s = Square(5, 0, 0, 12)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_str_passed_as_size(self):
        with self.assertRaises(TypeError) as exc:
            s = Square('10', 0, 0, 12)
        self.assertEqual('width must be an integer', str(exc.exception))

    def test_none_passed_as_size(self):
        with self.assertRaises(TypeError) as exc:
            s = Square(None, 0, 0, 12)
        self.assertEqual('width must be an integer', str(exc.exception))

    def test_tuple_passed_as_size(self):
        with self.assertRaises(TypeError) as exc:
            s = Square((2, 3), 0, 0, 12)
        self.assertEqual('width must be an integer', str(exc.exception))

    def test_list_passed_as_size(self):
        with self.assertRaises(TypeError) as exc:
            s = Square([1, 2, 3], 0, 0, 12)
        self.assertEqual('width must be an integer', str(exc.exception))

    def test_dict_passed_as_size(self):
        with self.assertRaises(TypeError) as exc:
            s = Square({'width': 10}, 0, 0, 12)
        self.assertEqual('width must be an integer', str(exc.exception))

    def test_obj_passed_as_size(self):
        with self.assertRaises(TypeError) as exc:
            s = Square(object, 0, 0, 12)
        self.assertEqual('width must be an integer', str(exc.exception))

    def test_zero_passed_as_size(self):
        with self.assertRaises(ValueError) as exc:
            s = Square(0, 0, 0, 12)
        self.assertEqual('width must be > 0', str(exc.exception))

    def test_neg_val_passed_as_size(self):
        with self.assertRaises(ValueError) as exc:
            s = Square(-5, 0, 0, 12)
        self.assertEqual('width must be > 0', str(exc.exception))

    def test_str_passed_as_x(self):
        with self.assertRaises(TypeError) as exc:
            s = Square(5, '0', 0, 12)
        self.assertEqual('x must be an integer', str(exc.exception))

    def test_none_passed_as_x(self):
        with self.assertRaises(TypeError) as exc:
            s = Square(5, None, 0, 12)
        self.assertEqual('x must be an integer', str(exc.exception))

    def test_tuple_passed_as_x(self):
        with self.assertRaises(TypeError) as exc:
            s = Square(5, (1, 2), 0, 12)
        self.assertEqual('x must be an integer', str(exc.exception))

    def test_list_passed_as_x(self):
        with self.assertRaises(TypeError) as exc:
            s = Square(5, [0, 1, 2], 0, 12)
        self.assertEqual('x must be an integer', str(exc.exception))

    def test_dict_passed_as_x(self):
        with self.assertRaises(TypeError) as exc:
            s = Square(5, {'x': 0}, 0, 12)
        self.assertEqual('x must be an integer', str(exc.exception))

    def test_obj_passed_as_x(self):
        with self.assertRaises(TypeError) as exc:
            s = Square(5, object, 0, 12)
        self.assertEqual('x must be an integer', str(exc.exception))

    def test_neg_val_passed_as_x(self):
        with self.assertRaises(ValueError) as exc:
            s = Square(5, -10, 0, 12)
        self.assertEqual('x must be >= 0', str(exc.exception))

    def test_str_passed_as_y(self):
        with self.assertRaises(TypeError) as exc:
            s = Square(5, 0, '0', 12)
        self.assertEqual('y must be an integer', str(exc.exception))

    def test_none_passed_as_y(self):
        with self.assertRaises(TypeError) as exc:
            s = Square(5, 0, None, 12)
        self.assertEqual('y must be an integer', str(exc.exception))

    def test_tuple_passed_as_y(self):
        with self.assertRaises(TypeError) as exc:
            s = Square(5, 0, (1, 2), 12)
        self.assertEqual('y must be an integer', str(exc.exception))

    def test_list_passed_as_y(self):
        with self.assertRaises(TypeError) as exc:
            s = Square(5, 0, [0, 1, 2], 12)
        self.assertEqual('y must be an integer', str(exc.exception))

    def test_dict_passed_as_y(self):
        with self.assertRaises(TypeError) as exc:
            s = Square(5, 0, {'x': 0}, 12)
        self.assertEqual('y must be an integer', str(exc.exception))

    def test_obj_passed_as_y(self):
        with self.assertRaises(TypeError) as exc:
            s = Square(5, 0, object, 12)
        self.assertEqual('y must be an integer', str(exc.exception))

    def test_neg_val_passed_as_y(self):
        with self.assertRaises(ValueError) as exc:
            s = Square(5, 0, -10, 12)
        self.assertEqual('y must be >= 0', str(exc.exception))

    def test_area_method(self):
        s = Square(5, 0, 0, 12)
        self.assertEqual(s.area(), 25)

    def test_display_method(self):
        s = Square(4)
        expected = "####\n####\n####\n####\n"
        captured = StringIO()

        with redirect_stdout(captured):
            s.display()

        actual = captured.getvalue()
        self.assertEqual(expected, actual)

    def test_overwritten_str_method(self):
        s = Square(5, 0, 0, 1)
        expected = "[Square] (1) 0/0 - 5"
        output = str(s)
        self.assertEqual(expected, output)

    def test_display_method_with_coordinates(self):
        s = Square(3, 1, 3)
        expected = "\n\n\n ###\n ###\n ###\n"

        captured = StringIO()
        with redirect_stdout(captured):
            s.display()

        actual = captured.getvalue()

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
