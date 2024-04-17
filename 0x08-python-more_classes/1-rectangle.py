#!/usr/bin/python3
""" This is my Rectangle Module """


class Rectangle:
    """ This is my Rectangle class """
    def __init__(self, width=0, height=0):
        """ init function to initialize """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter function """
        return self.__width

    @property
    def height(self):
        """ getter fucntion """
        return self.__height

    @width.setter
    def width(self, value):
        """ setter fucntion """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """ setter function """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
