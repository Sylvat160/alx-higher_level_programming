#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """Prints an integer with "{:d}".format().
    Prints "Exception: " followed by the exception
    description if value cannot be converted to an integer.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
