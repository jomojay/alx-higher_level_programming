#!/usr/bin/python3
"""101-add_attribute module"""


def add_attribute(obj, name, value):
    """checks if it can add attribute
    before adding it."""
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    elif hasattr(obj, "__slots__") and name in obj.__slots__:
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
