#!/usr/bin/python3
"""
    writes a string to a text file (UTF8) and
    returns the number of characters written
"""


def write_file(filename="", text=""):
    """ write file function """
    with open(filename, 'w', encoding='utf-8') as f:
        w = f.write(text)
    return w
