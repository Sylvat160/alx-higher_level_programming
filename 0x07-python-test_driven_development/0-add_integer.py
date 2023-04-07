#!/usr/bin/python3
""" Add Integer Module
    This module contains a function that adds two integers
"""


def add_integer(a, b=98):
    """adds two arguments(int or float)
    Args:
        a (int or float): first argument
        b (int or float): second argument
    Returns:
        int: the sum of a and b
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
