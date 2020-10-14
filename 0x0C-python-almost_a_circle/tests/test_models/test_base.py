#!/usr/bin/python3
"""Unittest for base
"""
import unittest
import pep8
from models.base import Base, __doc__


class TestBase(unittest.TestCase):
    """Test cases for max_integer function using unittest"""

    def test_docstring(self):
        """Test for docstrings"""
        self.assertIsNotNone(__doc__)
        self.assertIsNotNone(Base.__doc__)
        self.assertIs(hasattr(Base, "__init__"), True)
        self.assertIsNotNone(Base.__init__.__doc__)
        self.assertIsNotNone(Base.to_json_string.__doc__)
        self.assertIsNotNone(Base.from_json_string.__doc__)
        self.assertIsNotNone(Base.create.__doc__)
        self.assertIsNotNone(Base.load_from_file.__doc__)
        self.assertIsNotNone(Base.save_to_file_csv.__doc__)
        self.assertIsNotNone(Base.load_from_file_csv.__doc__)

    def test_pep8(self):
        """Test for pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/base.py"])
        self.assertEqual(result.total_errors, 0)

    def test_id(self):
        """Test for correct output"""
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()
        self.b4 = Base()
        self.b5 = Base()
        self.b6 = Base(13)
        self.b7 = Base("test")
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b4.id, 4)
        self.assertEqual(self.b5.id, 5)
        self.assertEqual(self.b6.id, 13)
        self.assertEqual(self.b7.id, "test")

    def test_type(self):
        """Test the type of an instance"""
        obj = Base()
        self.assertEqual(type(obj), Base)
