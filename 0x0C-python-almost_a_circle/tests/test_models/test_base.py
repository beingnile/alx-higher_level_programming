#!/usr/bin/python3
"""Tests the base class"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle


class BaseTestCase(unittest.TestCase):
    """TestCases for Base class"""
    def setUp(self):
        self.filename = 'Rectangle.json'

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_init_without_arg(self):
        """Test the id of an object when created without args"""
        b1 = Base()
        b2 = Base()
        self.assertIsInstance(b1, Base)
        self.assertIsInstance(b2, Base)
        self.assertNotEqual(b1.id, b2.id)

    def test_init_with_arg(self):
        """Test the id of an object when created with args"""
        b3 = Base(12)
        self.assertIsInstance(b3, Base)
        self.assertEqual(b3.id, 12)

    def test_alter_nb_objects(self):
        """Test nb_objects is a private class attribute.
        This testcase tests if the attribute can be altered by
        an object
        """
        b1 = Base()
        b2 = Base()
        with self.assertRaises(AttributeError):
            instance = b1.nb_objects

        b2.__nb_objects = 69
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_to_json_string(self):
        r = Rectangle(10, 7, 2, 8, 1)
        dictionary = r.to_dictionary()
        json_dict = Base.to_json_string([dictionary])
        expected = '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}]'

        self.assertEqual(json_dict, expected)

    def test_save_to_file(self):
        self.assertFalse(os.path.exists(self.filename))
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.exists(self.filename))
        exp = '[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}, {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]'
        with open(self.filename, 'r') as f:
            content = f.read()

        self.assertTrue(exp, content)
