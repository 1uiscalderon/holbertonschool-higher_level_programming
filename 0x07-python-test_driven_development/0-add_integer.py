#!/usr/bin/python3
"""Module that contains a simple function to add two integers.
This module must be imported to be used.
    -To run doctests:
        $ python3 -m doctest -v ./tests/0-add_integer.txt
"""


def add_integer(a, b=98):
    """Adds two integers
    Args:
        a: int to add.
        b: int to add.
    Returns:
        a + b
    Raises:
        TypeError: If a or b are not int or float.
"""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
