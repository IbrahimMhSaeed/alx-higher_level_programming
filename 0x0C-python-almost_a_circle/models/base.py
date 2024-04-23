#!/usr/bin/python3
""" Base Class Module """


class Base:
    """ Base Class for ID management """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialization function """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
