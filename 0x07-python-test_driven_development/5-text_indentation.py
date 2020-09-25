#!/usr/bin/python3
"""Module that contains a simple function prints a text with 2 new lines,
after each of these characters: ., ?.
This module must be imported to be used.
    -To run doctests:
        $ python3 -m doctest -v ./tests/5-text_indentation.txt
"""


def text_indentation(text):
    """Prints a square
    Args:
        size: Size of the square
    Raises:
        -TypeError: If arg is not an int
        -ValueError: If arg is negative
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.replace(".", ".\n\n").replace("?", "?\n\n")\
               .replace(":", ":\n\n")
    phrase = text.splitlines(True)
    result = ""
    for c in phrase:
        result += c.strip(" ")
    print(result, end="")
