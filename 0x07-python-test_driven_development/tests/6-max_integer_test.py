#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function using unittest"""

    def test_int(self):
        """Test for int"""
        self.assertEqual(max_integer([0,2,7,3,5]), 7)
        self.assertEqual(max_integer([0,2,-7,3,5]), 5)
        self.assertEqual(max_integer([-1,-2,-7,-3,-5]), -1)
        self.assertEqual(max_integer([2]), 2)
        self.assertEqual(max_integer([1,1,1,1,1]), 1)
        self.assertEqual(max_integer([2,5] * 3), 5)
    
    def test_empty(self):
        """Test with empty argument"""
        self.assertEqual(max_integer(), None)

    def test_wrong(self):
        """Test with different types"""
        with self.assertRaises(TypeError):
            li = max_integer([1,2,"j","l"])

    def test_None(self):
        """Test with None argument"""
        with self.assertRaises(TypeError):
            li = max_integer(None)
    
    def test_wrong2(self):
        """Test with different types"""
        with self.assertRaises(TypeError):
            li = max_integer((1,42))

    def test_float(self):
        """Test with different types float"""
        with self.assertRaises(TypeError):
            li = max_integer([2.3, 5.6, 7.8])
    
    def test_inf(self):
        """Checking for inf"""
        with self.assertRaises(TypeError):
            li = max_integer([float('inf'), 5.6, 7.8])

    def test_docstringmod(self):
        """Check docstring for module"""
        m = __import__('6-max_integer').__doc__
        self.assertTrue(m is not None and len(m) > 0)

    def test_docstringfunc(self):
        """Check docstring for Tests"""
        f = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(f is not None and len(f) > 5)

    def test_morethan(self):
        """Check arguments"""
        with self.assertRaises(TypeError):
            li = max_integer(1, 1)
        
if __name__ == '__main__':
    unittest.main()



    