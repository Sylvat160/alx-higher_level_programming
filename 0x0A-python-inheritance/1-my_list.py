#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    """A subclass of list"""
    def __init__(self):
        """Initialise the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        sorted_list = sorted(self)
        print(sorted_list)
