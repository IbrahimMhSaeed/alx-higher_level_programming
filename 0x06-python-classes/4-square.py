#!/usr/bin/python3


class Square:
    """ This is my square class """
    def __init__(self, size=0):
        """ This is my initailzer function """
        self.size = size

    @property
    def size(self):
        """ get size value """
        return self.__size

    @size.setter
    def size(self, value):
        """ Function to set size after checking """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Method computes square area """
        return self.__size ** 2
