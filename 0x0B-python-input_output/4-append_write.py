#!/usr/bin/python3
"""Append a string to a text file (UTF8) and returns the number of
   characters written"""


def append_write(filename="", text=""):
    """writes the string and return the number of char"""
    with open(filename, "a", encoding="utf8") as a_file:
        return a_file.write(text)
