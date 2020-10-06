#!/usr/bin/python3
""" inherits from BaseGeometry (7-base_geometry.py)."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class with inherated attributes from the rectangle"""

    def __init__(self, size):
        """Initializing Square Class"""

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Area """
        return self.__size * self.__size
