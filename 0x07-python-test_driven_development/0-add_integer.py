#!/usr/bin/python3
""" Add Integer Module
    This module contains a function that adds two integers
"""


def add_integer(a, b=98):
    """
    Adds 2 integers.

    Arguments:
    a -- an integer or float
    b -- an integer or float (default 98)

    Returns:
    The addition of a and b, casted to an integer.

    Raises:
    TypeError: if a or b is not an integer or float.
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer or b must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer or b must be an integer")

    return int(a) + int(b)

