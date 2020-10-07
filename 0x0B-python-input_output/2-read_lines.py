#!/usr/bin/python3
"""Returns the number of lines of a text file"""


def read_lines(filename="", nb_lines=0):
    """Reads a text file and return the number of lines"""
    lines = 0
    with open(filename) as a_file:
        i = len(list(a_file))
        if nb_lines >= i or nb_lines <= 0:
            nb_lines = i
        a_file.seek(0, 0)
        for l in range(nb_lines):
            print(a_file.readline(), end="")
