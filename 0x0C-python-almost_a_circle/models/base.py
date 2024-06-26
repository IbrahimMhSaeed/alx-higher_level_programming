#!/usr/bin/python3
""" Base Class Module """
import json


class Base:
    """ Base Class for ID management """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialization function """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def reset():
        Base.__nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to JSON string """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save to file method """
        if list_objs is None:
            list_objs = []

        dd = [x.to_dictionary() for x in list_objs]
        json_str = Base.to_json_string(dd)
        filename = f"{cls.__name__}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """ from json string method """
        if json_string is None:
            return []
        else:
            json_list = json.loads(json_string)
            return json_list

    @classmethod
    def create(cls, **dictionary):
        """ create method """
        if cls.__name__ == "Square":
            dummy = cls(size=1)
        else:
            dummy = cls(width=1, height=1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ load from file method """
        try:
            with open(f"{cls.__name__}.json") as f:
                content = f.read()
        except IOError:
            return []
        list_dict = cls.from_json_string(content)
        ins_list = []
        for ele in list_dict:
            temp = cls.create(**ele)
            ins_list.append(temp)
        return ins_list
