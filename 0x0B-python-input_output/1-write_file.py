#!/usr/bin/python3
"""Write a function that writes a string to a text file (UTF8)"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8)
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
