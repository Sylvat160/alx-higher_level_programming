#!/usr/bin.python3
"""Class Rectangle that defines a rectangle"""

class Rectangle:
    """Class Rectangle that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes the data
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """setter for width
        Args:
            value (int): width of the rectangle

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height
        Args:
            value (int): height of the rectangle

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
