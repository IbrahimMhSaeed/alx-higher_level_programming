#!/usr/bin/python3
""" class Student Module """


class Student:
    """ Student class """
    def __init__(self, first_name, last_name, age):
        """ init fuction """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ to json function """
        return self.__dict__
