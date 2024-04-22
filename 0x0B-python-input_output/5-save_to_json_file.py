#!/usr/bin/python3
""" save to json module """
import json


def save_to_json_file(my_obj, filename):
    """ save to json file """
    js = json.dumps(my_obj)
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(js)
