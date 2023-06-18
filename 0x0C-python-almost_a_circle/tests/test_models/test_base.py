#!/usr/bin/python3
"""Tests the base class"""
import unittest
from models.base import Base


class BaseTestCase(unittest.TestCase):
    """TestCases for Base class"""
    def setUp(self):
        self.b1 = Base()
        self.b2 = Base()

    def test_init_without_arg(self):
        """Test the id of an object when created without args"""
        self.assertIsInstance(self.b1, Base)
        self.assertIsInstance(self.b2, Base)
        self.assertNotEqual(self.b1.id, self.b2.id)

    def test_init_with_arg(self):
        """Test the id of an object when created with args"""
        b3 = Base(12)
        self.assertIsInstance(b3, Base)
        self.assertEqual(b3.id, 12)

    def test_alter_nb_instance(self):
        """Test nb_instance is a private class attribute.
        This testcase tests if the attribute can be altered by
        an object
        """
        with self.assertRaises(AttributeError):
            instance = self.b1.nb_instance

        self.b2.__nb_instance = 69
        b3 = Base()
        self.assertEqual(b3.id, 3)
