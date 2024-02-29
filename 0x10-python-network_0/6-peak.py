#!/usr/bin/python3
""" a function to find an element in list whose neighbors are both < it"""


def find_peak(list_of_integers):
    """
    Return the peak in a list of integers
    """
    if len(list_of_integers) > 0:
        list_of_integers.sort()
        return list_of_integers[-1]
    else:
        return None
