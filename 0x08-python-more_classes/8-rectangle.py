#!/usr/bin/python3
"""first class"""


class Rectangle:
    """Class that defines a Rectangle
        - Attributes:
                -width: width of a rectangle
                -height: height of a rectangle
        - Raises:
                -TypeError: If not an int
                -ValueError: If passed a negative number
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """instance initializing"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """return value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """variable initializing"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """return value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """variable initializing"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Area of Rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns perimeter of rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ Prints rectangle using the # symbol"""
        print_rec = ""
        if self.__width == 0 or self.__height == 0:
            return print_rec
        else:
            for i in range(self.__height):
                print_rec += str(self.print_symbol) * self.__width + "\n"
            return print_rec[:-1]

    def __repr__(self):
        """ Prints the info of the rectangle """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """ Prints message when deleted """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method to compare the rectangles by area"""
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        elif rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
