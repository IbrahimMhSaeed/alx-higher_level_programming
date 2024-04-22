#!/usr/bin/python3
""" class Student Module """


class Student:
    """ Student class """
    def __init__(self, first_name, last_name, age):
        """ init fuction """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ to json function """
        if not attrs:
            return self.__dict__
        for attr in attrs:
            if not isinstance(attr, str):
                break
        else:
            ans = {}
            for attr in attrs:
                if attr in self.__dict__:
                    ans[attr] = self.__dict__[attr]
            return ans

        return self.__dict__
