#!/usr/bin/python3
""" Base Class Module """
import json


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
        json_list = json.loads(json_string)
        if json_list is None:
            return list()
        else:
            return json_list

    @classmethod
    def create(cls, **dictionary):
        """ create method """
        dummy = cls(1, 1, 0, 0)
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
