#!/usr/bin/python3
"""0-lookup module
"""


def lookup(obj):
    """lookup - function that returns the list of available
    attributes and methods of an object.
    Args:
        obj (object): an object to be looked up
    Return: list of attributes and methods of the object
    """
    return dir(obj)
