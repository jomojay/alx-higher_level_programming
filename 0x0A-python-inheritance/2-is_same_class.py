#!/usr/bin/python3
"""2-is_same_class module"""


def is_same_class(obj, a_class):
    """check if object is exactly and instance of given class
    Args:
        obj: the object we're checking
        a_class: the class we are checking
    Return:
        True is obj is an instance of the class
        False if not
    """
    return type(obj) is a_class
