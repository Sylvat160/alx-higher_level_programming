#!/usr/bin/python3
lookup = __import__('0-lookup').lookup

"""
test 0-lookup.py
"""


class MyClasse(object):
    pass


class MyClasse2(object):
    attr = 2
    def my_def(self):
        pass


print(lookup(MyClasse))
print(lookup(MyClasse2))
print(lookup(int))
