#!/usr/bin/python3

IsSame = __import__('2-is_same_class').is_same_class

a = 3
if IsSame(a, int) :
    print("{} is an instance of the class {}".format(a, int.__name__))
if IsSame(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if IsSame(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))
