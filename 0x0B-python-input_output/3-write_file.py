#!/usr/bin/python3
"""Writes a string to a text file (UTF8) and returns the number of
   characters written"""


def write_file(filename="", text=""):
    """writes the string and return the number of char"""
    with open(filename, "w", encoding="utf8") as a_file:
        return a_file.write(text)
