#!/usr/bin/python3
"""base.py module that contains a Base class"""


class Base:
    """Base class for all future classes
    Attribute
        __nb_objects (int): a private class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """a constructor for object instance definition
        args:
            id (int): id of the object instance
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
