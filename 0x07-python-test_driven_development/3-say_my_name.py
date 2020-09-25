#!/usr/bin/python3
"""Module that contains a simple function to divides all elements of a matrix.
This module must be imported to be used.
    -To run doctests:
        $ python3 -m doctest -v ./tests/2-matrix_divided.txt
"""


def say_my_name(first_name, last_name=""):
    """Divides a matrix by a Number
    Args:
        first_name: String with a first name.
        last_name: String with a last name.
    Raises:
        -TypeError: If an arg is not a string.
"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
