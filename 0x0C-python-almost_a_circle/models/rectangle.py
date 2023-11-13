#!/usr/bin/python3
'''rectangle.py module'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle - a sub class of Base class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''init constructor
        args:
            width (int): width of Rectangle
            height (int): height of Rectangle
            x (int):
            y (int):
            id (int): id of the object instance
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''get width of a rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''set width of a rectangle'''
        self.validator("width", value, False)
        self.__width = value

    @property
    def height(self):
        '''get height of a rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''set height of a rectangle'''
        self.validator("height", value, False)
        self.__height = value

    @property
    def x(self):
        '''get x of a rectangle'''
        return self.__x

    @x.setter
    def x(self, value):
        '''set x of a rectangle'''
        self.validator("x", value)
        self.__x = value

    @property
    def y(self):
        '''get y of a rectangle'''
        return self.__y

    @y.setter
    def y(self, value):
        '''set y of a rectangle'''
        self.validator("y", value)
        self.__y = value

    def validator(self, name, value, eq=True):
        '''validator - check the value as int and >= 0
        args:
            name (str): name of the attribute
            value (int): value of the attribute
            eq: always true
        '''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        '''find area of a rectangle'''
        return self.width * self.height

    def display(self):
        '''to print string rep of a rectangle'''
        rep = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(rep, end='')

    def __str__(self):
        '''str info about a rectangle'''
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        '''update instance attributes via */**args'''
        if id:
            self.id = id
        if width:
            self.width = width
        if height:
            self.height = height
        if x:
            self.x = x
        if y:
            self.y = y

    def update(self, *args, **kwargs):
        '''update instance attributes via */** args'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''dictionary rep of a class'''
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
