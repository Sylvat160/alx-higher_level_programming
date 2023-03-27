#!/usr/bin/python3

def safe_print_division(a, b):
    """Divides 2 integers and prints the result.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        The value of the division, otherwise None.
    """
    try:
        div = (a / b)
    except (ZeroDivisionError, TypeError):
        return (None)
    finally:
        print("Inside result: {}".format(div))
    return (div)
