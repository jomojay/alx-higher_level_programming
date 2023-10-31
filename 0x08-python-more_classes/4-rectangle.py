#!/usr/bin/python3
"""4-rectangle module"""


class Rectangle:
    """defines a Rectangle class"""

    def __init__(self, width=0, height=0):
        """init rectangle
        Args:
            width (int): the width
            height (int): the height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """property of width
        Returns: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """set the width
        Args:
            value: to set the width
        Raises:
            TypeError: if width is not int
            ValueError: if width < 0
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """property of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height
        Args:
            value (int): to set the height to
        Raises:
            TypeError: if value is not int
            ValueError: if value < 0
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """return the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """return the perimeter of the rectangle"""
        if not self.width or not self.height:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """return the string rep of rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        return (("#" * self.width + "\n") * self.height)[:-1]

    def __repr__(self):
        """return a formal representation of rectangles"""
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"
