#!/usr/bin/python3
"""1-my_list module"""


class MyList(list):
    """MyList class that inherits from list"""

    def print_sorted(self):
        """print_sorted - prints the list in a sorted
        (ascending sort) other
        args:
            self (MyList object)
        """
        print(sorted(self))
