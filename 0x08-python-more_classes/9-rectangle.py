#!/usr/bin/python3
"""9-rectangle module"""


class Rectangle:
    """defines a Rectangle class
    Attributes:
        number_of_instances (int)
        print_symbol
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """init rectangle
        Args:
            width (int): the width
            height (int): the height
            number_of_instances (int): obj count
        """
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

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
            value (int): to set the width to
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
        """the property of height
        Reyturn: heigjt of rectangle"""
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
        return ((str(self.print_symbol) * self.width + "\n") *
                self.height)[:-1]

    def __repr__(self):
        """return a formal representation of rectangles"""
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """when you delete a rectangle"""
        print("Bye rectangle...")
        self.__class__.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''to return the bigger of two rectangles
        Args:
            rect_1: rectangle obj
            rect_2: rectangle obj
        Raises:
            TypeError: if rect_1 or rect_2 are not rectangles
        Returns:
            rectangle with the greater area or rect_1 if equal
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """to create a square
        Args:
            size: the size of square
        """
        return cls(size, size)
