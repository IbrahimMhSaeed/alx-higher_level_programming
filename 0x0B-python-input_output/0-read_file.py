#!/usr/bin/python3
""" Read text file in utf-8 """


def read_file(filename=""):
    """ read file function """
    with open(filename, encoding='utf-8') as f:
        content = f.read()
    print(content, end="")
