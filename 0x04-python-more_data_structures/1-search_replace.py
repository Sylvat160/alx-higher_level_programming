#!/usr/bin/python3

def search_replace(my_list, search, replace):
    i = my_list.index(search)
    my_list[i] = replace
    return my_list
