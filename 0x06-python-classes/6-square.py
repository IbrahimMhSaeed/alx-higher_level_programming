#!/usr/bin/python3
""" This is my square module """


class Square:
    """ This is my square class """
    def __init__(self, size=0, position=(0, 0)):
        """ This is my initailzer function """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ get size value """
        return self.__size
    @property
    def position(self):
        """ get position of square """
        return self.__position

    @size.setter
    def size(self, value):
        """ Function to set size after checking """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """ Set value of position after some checks """
        if type(value) == tuple and len(value) == 2:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ Method computes square area """
        return self.__size ** 2

    def my_print(self):
        """ Print the square """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
