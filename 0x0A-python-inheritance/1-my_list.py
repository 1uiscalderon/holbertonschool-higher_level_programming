#!/usr/bin/python3
"""Class MyList that inherits from list"""


class MyList(list):
    """MyList that inherits from list"""

    def print_sorted(self):
        """Prints the list, but sorted"""
        print(sorted(self))
