#!/usr/bin/python3
"""Unittest for base
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle, __doc__ as mrdoc
import inspect
import pep8
from contextlib import redirect_stdout
from io import StringIO


class TestRectangle(unittest.TestCase):
    """Test cases for max_integer function using unittest"""
    def test_doctstring(self):
        """Checks doctstring for base class"""
        self.assertTrue(len(mrdoc.strip()) > 0)
        self.assertTrue(len(Base.__doc__.strip()) > 0)
        functions = inspect.getmembers(Base, predicate=inspect.ismethod)
        for name, func in functions:
            self.assertTrue(len(func.__doc__.strip()) > 0)
        functions = inspect.getmembers(Base, predicate=inspect.isfunction)
        for name, func in functions:
            self.assertTrue(len(func.__doc__.strip()) > 0)

    def test_rectangle(self):
        """Checks correct usage of rectangle"""
        r = Rectangle(2, 2)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 2)

    def test_pep8(self):
        """Test for pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/rectangle.py"])
        self.assertEqual(result.total_errors, 0)

    def test_error(self):
        """Test for error"""
        with self.assertRaises(TypeError):
            r = Rectangle()
        with self.assertRaises(TypeError):
            r = Rectangle(1)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, 4, 5, 6)

    def test_float(self):
        """Test for Float inputs"""
        with self.assertRaises(TypeError):
            r = Rectangle(2.0, 3)
        with self.assertRaises(TypeError):
            r = Rectangle(float('inf', 2))

    def test_string(self):
        """Test with a string"""
        with self.assertRaises(TypeError):
            r = Rectangle(float("Test", 2))

    def test_negative_numbers(self):
        """Using negative numbers"""
        with self.assertRaises(ValueError):
            r = Rectangle(-2, 2)

    def test_area(self):
        """Checking area"""
        r = Rectangle(1, 2)
        self.assertEqual(r.area(), 2)

    def test_display(self):
        """Check display function"""
        r = Rectangle(3, 3)
        stout = StringIO()
        with redirect_stdout(stout):
            r.display()
        out = stout.getvalue()
        self.assertEqual(out, ("#" * 3 + "\n") * 3)

    def test_str(self):
        """Test for str"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")

if __name__ == '__main__':
    unittest.main()
