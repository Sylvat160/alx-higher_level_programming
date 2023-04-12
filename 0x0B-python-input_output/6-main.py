#!/usr/bin/python3

loadFromJsonFile = __import__('6-load_from_json_file').load_from_json_file


try:
    my_list = loadFromJsonFile("my_list.json")
    print(my_list)
except:
    my_list = []
    print("File doesn't exist")

# print("My list: {}".format(my_list))