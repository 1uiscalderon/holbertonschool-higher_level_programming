#!/usr/bin/python3
"""Module that contains a simple function to print a square.
    This module must be imported to be used.
        -To run doctests:
            $ python3 -m doctest -v ./tests/4-print_square.txt
"""


def print_square(size):
    """Prints a square
        Args:
            size: Size of the square
        Raises:
            -TypeError: If arg is not an int
            -ValueError: If arg is negative
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
