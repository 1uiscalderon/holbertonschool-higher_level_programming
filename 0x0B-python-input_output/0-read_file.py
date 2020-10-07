#!/usr/bin/python3
"""Reads a text file"""


def read_file(filename=""):
    """Reads a text file"""
    with open(filename, encoding="utf8") as a_file:
        print(a_file.read())
