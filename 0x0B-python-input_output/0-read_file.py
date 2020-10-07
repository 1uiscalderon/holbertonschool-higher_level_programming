#!/usr/bin/python3
"""Reads a text file"""


def read_file(filename=""):
    """Reads a text file"""

    with open(filename) as a_file:
        print(a_file.read())
