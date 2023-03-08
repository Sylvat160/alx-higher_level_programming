#!/usr/bin/python3

def print_last_digit(number):
    """Prints the last digit of a number.

    Args:
        number (int): The number to print the last digit of.

    Returns:
        int: The last digit of the number.
    """
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit
