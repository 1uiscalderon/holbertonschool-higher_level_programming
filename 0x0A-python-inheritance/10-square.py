#!/usr/bin/python3
""" inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class with inherated attributes from the rectangle"""

    def __init__(self, size):
        """Initializing Square Class"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Area """
        return self.__size * self.__size
