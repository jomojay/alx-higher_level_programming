#!/usr/bin/python3
"""1-rectangle module"""


class Rectangle:
    """defines a Rectangle class"""

    def __init__(self, width=0, height=0):
        """initializes rectangle attributes
        Args:
            width (int): the width
            height(int): the height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """property of width to get and return it
        Returns: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """set the width
        Args:
            value (int): to set the width
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
        """property of height to get and return it"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height
        Args:
            value (int): to set the height
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
