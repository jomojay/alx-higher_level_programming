#!/usr/bin/python3
"""3-is_kind_of_class module"""


def is_kind_of_class(obj, a_class):
    """checks if obj is of a sublass of a_class
    Args:
        obj: the object
        a_class: the class we are checking it for
    Return:
        True or False
    """
    return isinstance(obj, a_class)
