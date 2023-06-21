#!/usr/bin/python3
"""Test Square class"""
import os
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

    def test_float_passed_as_size(self):
        with self.assertRaises(TypeError) as exc:
            s = Square(5.5, 0, 0, 12)
        self.assertEqual('width must be an integer', str(exc.exception))

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

    def test_float_passed_as_x(self):
        with self.assertRaises(TypeError) as exc:
            s = Square(5, 5.5, 0, 12)
        self.assertEqual('x must be an integer', str(exc.exception))

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

    def test_float_passed_as_y(self):
        with self.assertRaises(TypeError) as exc:
            s = Square(5, 0, 5.5, 12)
        self.assertEqual('y must be an integer', str(exc.exception))

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

    def test_update_method(self):
        s = Square(5, 0, 0, 1)
        self.assertEqual('[Square] (1) 0/0 - 5', str(s))
        s.update(10)
        self.assertEqual('[Square] (10) 0/0 - 5', str(s))
        s.update(1, 2, x=12)
        self.assertEqual('[Square] (1) 0/0 - 2', str(s))
        s.update(1, 2, 3, 4)
        self.assertEqual('[Square] (1) 3/4 - 2', str(s))
        s.update(x=12)
        self.assertEqual('[Square] (1) 12/4 - 2', str(s))
        s.update(size=7, y=1)
        self.assertEqual('[Square] (1) 12/1 - 7', str(s))
        s.update(size=7, id=89, y=1)
        self.assertEqual('[Square] (89) 12/1 - 7', str(s))

    def test_to_dictionary_method(self):
        s = Square(10, 2, 1, 1)
        s_dict = s.to_dictionary()
        expected = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(s_dict, expected)

    def test_save_to_file(self):
        filename = "Square.json"

        if os.path.exists(filename):
            os.remove(filename)

        self.assertFalse(os.path.exists(filename))
        s1 = Square(10, 2, 8, 1)
        s2 = Square(2, 0, 0, 2)
        Square.save_to_file([s1, s2])
        self.assertTrue(os.path.exists(filename))
        exp = '[{"y": 8, "x": 2, "id": 1, "size": 10}, {"y": 0, "x": 0, "id": 2, "size": 2}]'
        with open(filename, 'r') as f:
            content = f.read()

        self.assertTrue(exp, content)

    def test_none_save_to_file(self):
        filename = "Square.json"

        if os.path.exists(filename):
            os.remove(filename)

        self.assertFalse(os.path.exists(filename))
        Square.save_to_file(None)
        self.assertTrue(os.path.exists(filename))
        exp = '[]'
        with open(filename, 'r') as f:
            content = f.read()

        self.assertTrue(exp, content)

    def test_empty_list_save_to_file(self):
        filename = "Square.json"

        if os.path.exists(filename):
            os.remove(filename)

        self.assertFalse(os.path.exists(filename))
        Square.save_to_file([])
        self.assertTrue(os.path.exists(filename))
        exp = '[]'
        with open(filename, 'r') as f:
            content = f.read()

        self.assertTrue(exp, content)

    def test_from_json_string_none_arg(self):
        list_output = Square.from_json_string(None)
        self.assertTrue(type(list_output) == list)
        self.assertListEqual(list_output, [])

    def test_from_json_string_empty_str_arg(self):
        list_output = Square.from_json_string("")
        self.assertTrue(type(list_output) == list)
        self.assertListEqual(list_output, [])

    def test_from_json_string(self):
        list_input = [
            {'id': 89, 'size': 10},
            {'id': 7, 'size': 1}
        ]
        json_str_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_str_input)
        self.assertTrue(type(list_output) == list)
        self.assertListEqual(list_output, list_input)

    def test_create(self):
        s = Square(3, 1, 0, 1)
        s_dict = s.to_dictionary()
        s1 = Square.create(**s_dict)
        self.assertEqual(str(s), '[Square] (1) 1/0 - 3')
        self.assertEqual(str(s1), '[Square] (1) 1/0 - 3')
        self.assertNotEqual(s, s1)
        self.assertFalse(s is s1)


if __name__ == '__main__':
    unittest.main()
