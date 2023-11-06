#!/usr/bin/python3
"""9-rectangle module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class - a subclass of BaseGeometry"""
    def __init__(self, width, height):
        """init method
        args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns the area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """str representation method for rectangle"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
