#!/usr/bin/python3

def search_replace(my_list, search, replace):
    return [replace if c == search else c for c in my_list]
