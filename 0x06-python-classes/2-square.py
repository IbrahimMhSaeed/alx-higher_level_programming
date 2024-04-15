#!/usr/bin/python3
""" This is my Square module """


class Square:
    """ This is my square class """
    def __init__(self, size=0):
        """ This is my initailzer function """
        self.set_size(size)

    def set_size(self, size):
        """ Function to set size after checking """
        if size is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
