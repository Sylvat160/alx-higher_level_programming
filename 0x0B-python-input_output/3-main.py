#!/usr/bin/python3

toJSONString = __import__('3-to_json_string').to_json_string

my_list = [1, 2, 3]
my_obj = {
    'id': 12,
    'name': "John",
    'places': ["San Francisco", "Tokyo"],
    'is_active': True}

print(toJSONString(my_obj))