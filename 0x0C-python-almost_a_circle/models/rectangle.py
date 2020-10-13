#!/usr/bin/python3
"""Creating module with rectangle Class"""
from models.base import Base


class Rectangle(Base):
    """Inherits the attributes of the Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize class Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def validator(self, name, value):
        """Verify conditions"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        elif name in ["width", "height"] and value <= 0:
            raise ValueError("{:s} must be > 0".format(name))
        elif name in ["x", "y"] and value < 0:
            raise ValueError("{:s} must be >= 0".format(name))

    @property
    def width(self):
        """Getter of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        self.validator("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        self.validator("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for width"""
        self.validator("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        self.validator("y", value)
        self.__y = value

    def area(self):
        """Defines area"""
        return self.__width * self.__height

    def display(self):
        """Print rectangle using #"""
        print("\n" * self.__x, end="")
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Returns a string"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        attributes = ["id", "width", "height", "x", "y"]
        for attri, arg in zip(attributes, args):
            setattr(self, attri, arg)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """return dictionary representation"""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
