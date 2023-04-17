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

    def __init__(self, id=None):
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

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string
        Args:
            json_string (str): string representing a list of dictionaries
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set
        Args:
            **dictionary (dict): double pointer to a dictionary
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as json_file:
                list_dicts = Base.from_json_string(json_file.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV string representation of list_objs to a file
        Args:
            list_objs (list): list of instances who inherits of Base
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w') as csv_file:
            if list_objs is None or list_objs == []:
                csv_file.write("[]")
            else:
                if cls.__name__ == "Recangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csv_file, fieldnames=fields)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        Reads from `<cls.__name__>.csv`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
