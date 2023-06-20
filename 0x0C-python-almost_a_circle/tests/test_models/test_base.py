#!/usr/bin/python3
"""Tests the base class"""
import unittest
from models.base import Base


class BaseTestCase(unittest.TestCase):
    """TestCases for Base class"""
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
