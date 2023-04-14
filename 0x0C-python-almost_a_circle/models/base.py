#!/usr/bin/python3
"""Module for Base class"""


import json
import csv
import turtle


class Base:
    """The Base classs
    Attributes:
        __nb_objects (int): number of objects
    """

    __nb_objects = 0

    def __init__(self, id=None) :
        """Base class constructor
        Args:
            id (int): id of the object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries
        Args:
            list_dictionaries (list): list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file
        Args:
            list_objs (list): list of instances who inherits of Base
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                json_file.write(Base.to_json_string(list_dicts))