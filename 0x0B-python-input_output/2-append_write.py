#!/usr/bin/python3
"""
    appends a string at the end of a text file (UTF8) and
    returns the number of characters added
"""


def append_write(filename="", text=""):
    """ append write funciton """
    with open(filename, 'a', encoding='utf-8') as f:
        a = f.write(text)
    return a
