#!/usr/bin/python3
"""100-my_int module"""


class MyInt(int):
    """MyInt - a subclass of int class"""
    def __eq__(self, other):
        """myint is a rebel, eq is !="""
        return super().__ne__(other)

    def __ne__(self, other):
        """myint is a rebel, ne is =="""
        return super().__eq__(other)
