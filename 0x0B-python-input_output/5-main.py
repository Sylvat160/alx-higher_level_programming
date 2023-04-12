#!/usr/bin/python3

saveToJSONFile = __import__('5-save_to_json_file').save_to_json_file


my_list = [1, 2, 3]
my_obj = {
    'id': 12,
    'name': "John",
    'places': ["San Francisco", "Tokyo"],
    'is_active': True}

saveToJSONFile(my_obj, "my_list.json")