#!/usr/bin/python3
"""Unittest for base
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square, __doc__ as mrdoc
import inspect
import pep8
from contextlib import redirect_stdout
from io import StringIO


class TestSquare(unittest.TestCase):
    """Test cases for max_integer function using unittest"""
    def test_doctstring(self):
        """Checks doctstring for base class"""
        self.assertTrue(len(mrdoc.strip()) > 0)
        self.assertTrue(len(Square.__doc__.strip()) > 0)
        functions = inspect.getmembers(Square, predicate=inspect.ismethod)
        for name, func in functions:
            self.assertTrue(len(func.__doc__.strip()) > 0)
        functions = inspect.getmembers(Square, predicate=inspect.isfunction)
        for name, func in functions:
            self.assertTrue(len(func.__doc__.strip()) > 0)

    def test_square(self):
        """Checks correct usage of square"""
        s = Square(2, 2)
        self.assertEqual(s.size, 2)

    def test_raise(self):
        """Checking for errors"""
        with self.assertRaises(TypeError):
            Square(10.0)
    
    def test_str(self):
        """Test for str"""
        s1 = Square(4, 2, 1, 12)
        self.assertEqual(s1.__str__(), "[Square] (12) 2/1 - 4")
