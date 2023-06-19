#!/usr/bin/python3
"""Test Rectangle class"""
import unittest
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
