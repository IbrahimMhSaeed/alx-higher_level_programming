#!/usr/bin/python3
""" Rectangle Module """
from models.base import Base


class Rectangle(Base):
    """ Rectangle Class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init function """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width getter """
        return self.__width

    @property
    def height(self):
        """ height getter """
        return self.__height

    @property
    def x(self):
        """ x getter """
        return self.__x

    @property
    def y(self):
        """ y getter """
        return self.__y

    @width.setter
    def width(self, value):
        """ width setter """
        self.__width = value

    @height.setter
    def height(self, value):
        """ height setter """
        self.__height = value

    @x.setter
    def x(self, value):
        """ x setter """
        self.__x = value

    @y.setter
    def y(self, value):
        """ y setter """
        self.__y = value