#!/usr/bin/python3
""" Empty class Square that defines a square
    Attributes:
        size type int: size of the square
    """


class Square:
    """Square as a Class"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialization of attributes"""
        self.__size = size
        self.__position = position

    def area(self):
        """defines area of the Square"""
        return self.__size ** 2

    def my_print(self):
        """prints the Square"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)

    @property
    def size(self):
        """Defines size of Square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Defines size of Square with a value entered"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Defines position of Square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Defines position of Square with a value entered"""
        if type(value) is not tuple or len(value) != 2 or\
           type(value[0]) is not int or type(value[1]) is not int or\
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
