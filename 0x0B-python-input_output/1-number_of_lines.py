#!/usr/bin/python3
"""Returns the number of lines of a text file"""


def number_of_lines(filename=""):
    """Reads a text file and return the number of lines"""
    lines = 0
    with open(filename, encoding="utf8") as a_file:
        for l in a_file:
            lines += 1
    return lines
