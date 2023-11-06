#!/usr/bin/python3
"""11-square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square - a sublass of Rectangle class"""
    def __init__(self, size):
        """init method
        args:
            size (int): size of square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """get the area of square"""
        return self.__size * self.__size

    def __str__(self):
        """to return the string rep of square"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
