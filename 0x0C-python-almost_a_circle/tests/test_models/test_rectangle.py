#!/usr/bin/python3
"""Test Rectangle class"""
import unittest
from io import StringIO
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle


class RectangleTestCase(unittest.TestCase):
    """Defines all test cases for the Rectangle class"""
    def test_subclass_check(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def test_rectangle_id(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        self.assertNotEqual(r1.id, r2.id)

    def test_no_params(self):
        with self.assertRaises(TypeError):
            r4 = Rectangle()

    def test_x_and_y_params(self):
        r5 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r5.x, 0)
        self.assertEqual(r5.y, 0)

    def test_width_and_height_params(self):
        r6 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r6.width, 10)
        self.assertEqual(r6.height, 2)

    def test_str_passed_as_width(self):
        with self.assertRaises(TypeError) as exc:
            r = Rectangle('10', 2, 0, 0, 12)
        self.assertEqual('width must be an integer', str(exc.exception))

    def test_none_passed_as_width(self):
        with self.assertRaises(TypeError) as exc:
            r = Rectangle(None, 2, 0, 0, 12)
        self.assertEqual('width must be an integer', str(exc.exception))

    def test_tuple_passed_as_width(self):
        with self.assertRaises(TypeError) as exc:
            r = Rectangle((2, 3), 2, 0, 0, 12)
        self.assertEqual('width must be an integer', str(exc.exception))

    def test_list_passed_as_width(self):
        with self.assertRaises(TypeError) as exc:
            r = Rectangle([1, 2, 3], 2, 0, 0, 12)
        self.assertEqual('width must be an integer', str(exc.exception))

    def test_dict_passed_as_width(self):
        with self.assertRaises(TypeError) as exc:
            r = Rectangle({'width': 10}, 2, 0, 0, 12)
        self.assertEqual('width must be an integer', str(exc.exception))

    def test_obj_passed_as_width(self):
        with self.assertRaises(TypeError) as exc:
            r = Rectangle(object, 2, 0, 0, 12)
        self.assertEqual('width must be an integer', str(exc.exception))

    def test_zero_passed_as_width(self):
        with self.assertRaises(ValueError) as exc:
            r = Rectangle(0, 2, 0, 0, 12)
        self.assertEqual('width must be > 0', str(exc.exception))

    def test_neg_val_passed_as_width(self):
        with self.assertRaises(ValueError) as exc:
            r = Rectangle(-10, 2, 0, 0, 12)
        self.assertEqual('width must be > 0', str(exc.exception))

    def test_str_passed_as_height(self):
        with self.assertRaises(TypeError) as exc:
            r = Rectangle(10, '2', 0, 0, 12)
        self.assertEqual('height must be an integer', str(exc.exception))

    def test_none_passed_as_height(self):
        with self.assertRaises(TypeError) as exc:
            r = Rectangle(10, None, 0, 0, 12)
        self.assertEqual('height must be an integer', str(exc.exception))

    def test_tuple_passed_as_height(self):
        with self.assertRaises(TypeError) as exc:
            r = Rectangle(10, (2, 3), 0, 0, 12)
        self.assertEqual('height must be an integer', str(exc.exception))

    def test_list_passed_as_height(self):
        with self.assertRaises(TypeError) as exc:
            r = Rectangle(10, [1, 2, 3], 0, 0, 12)
        self.assertEqual('height must be an integer', str(exc.exception))

    def test_dict_passed_as_height(self):
        with self.assertRaises(TypeError) as exc:
            r = Rectangle(10, {'width': 10}, 0, 0, 12)
        self.assertEqual('height must be an integer', str(exc.exception))

    def test_obj_passed_as_height(self):
        with self.assertRaises(TypeError) as exc:
            r = Rectangle(10, object, 0, 0, 12)
        self.assertEqual('height must be an integer', str(exc.exception))

    def test_zero_passed_as_height(self):
        with self.assertRaises(ValueError) as exc:
            r = Rectangle(10, 0, 0, 0, 12)
        self.assertEqual('height must be > 0', str(exc.exception))

    def test_neg_val_passed_as_height(self):
        with self.assertRaises(ValueError) as exc:
            r = Rectangle(10, -2, 0, 0, 12)
        self.assertEqual('height must be > 0', str(exc.exception))

    def test_str_passed_as_x(self):
        with self.assertRaises(TypeError) as exc:
            r = Rectangle(10, 2, '0', 0, 12)
        self.assertEqual('x must be an integer', str(exc.exception))

    def test_none_passed_as_x(self):
        with self.assertRaises(TypeError) as exc:
            r = Rectangle(10, 2, None, 0, 12)
        self.assertEqual('x must be an integer', str(exc.exception))

    def test_tuple_passed_as_x(self):
        with self.assertRaises(TypeError) as exc:
            r = Rectangle(10, 2, (1, 2), 0, 12)
        self.assertEqual('x must be an integer', str(exc.exception))

    def test_list_passed_as_x(self):
        with self.assertRaises(TypeError) as exc:
            r = Rectangle(10, 2, [0, 1, 2], 0, 12)
        self.assertEqual('x must be an integer', str(exc.exception))

    def test_dict_passed_as_x(self):
        with self.assertRaises(TypeError) as exc:
            r = Rectangle(10, 2, {'x': 0}, 0, 12)
        self.assertEqual('x must be an integer', str(exc.exception))

    def test_obj_passed_as_x(self):
        with self.assertRaises(TypeError) as exc:
            r = Rectangle(10, 2, object, 0, 12)
        self.assertEqual('x must be an integer', str(exc.exception))

    def test_neg_val_passed_as_x(self):
        with self.assertRaises(ValueError) as exc:
            r = Rectangle(10, 2, -10, 0, 12)
        self.assertEqual('x must be >= 0', str(exc.exception))

    def test_str_passed_as_y(self):
        with self.assertRaises(TypeError) as exc:
            r = Rectangle(10, 2, 0, '0', 12)
        self.assertEqual('y must be an integer', str(exc.exception))

    def test_none_passed_as_y(self):
        with self.assertRaises(TypeError) as exc:
            r = Rectangle(10, 2, 0, None, 12)
        self.assertEqual('y must be an integer', str(exc.exception))

    def test_tuple_passed_as_y(self):
        with self.assertRaises(TypeError) as exc:
            r = Rectangle(10, 2, 0, (1, 2), 12)
        self.assertEqual('y must be an integer', str(exc.exception))

    def test_list_passed_as_y(self):
        with self.assertRaises(TypeError) as exc:
            r = Rectangle(10, 2, 0, [0, 1, 2], 12)
        self.assertEqual('y must be an integer', str(exc.exception))

    def test_dict_passed_as_y(self):
        with self.assertRaises(TypeError) as exc:
            r = Rectangle(10, 2, 0, {'x': 0}, 12)
        self.assertEqual('y must be an integer', str(exc.exception))

    def test_obj_passed_as_y(self):
        with self.assertRaises(TypeError) as exc:
            r = Rectangle(10, 2, 0, object, 12)
        self.assertEqual('y must be an integer', str(exc.exception))

    def test_neg_val_passed_as_y(self):
        with self.assertRaises(ValueError) as exc:
            r = Rectangle(10, 2, 0, -10, 12)
        self.assertEqual('y must be >= 0', str(exc.exception))

    def test_area_method(self):
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.area(), 20)

    def test_display_method(self):
        """The display method prints the rectangle figure to stdout
        using #.

        Testing this requires some sort of way of capturing the stdout
        value when running r.display(), and therefore StringIO is employed
        """
        r = Rectangle(4, 2)
        expected = "####\n####\n"
        captured = StringIO()

        with redirect_stdout(captured):
            r.display()

        actual = captured.getvalue()
        self.assertEqual(expected, actual)

    def test_overwritten_str_method(self):
        r = Rectangle(4, 6, 2, 1, 12)
        expected = "[Rectangle] (12) 2/1 - 4/6"
        output = str(r)
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
