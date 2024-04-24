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

    def __getattr__(self, name):
        """ Generic Getter """
        return self.__dict__[f"__{name}"]

    def __setattr__(self, name, value):
        """ Generic Setter """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if name == "width" or name == "height":
            if value <= 0:
                raise ValueError(f"{name} must be > 0")
        if name == "x" or name == "y":
            if value < 0:
                raise ValueError(f"{name} must be >= 0")

        self.__dict__[f"__{name}"] = value

    def area(self):
        """ compute area method """
        return self.width * self.height

    def display(self):
        """ display rectangle """
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """ string printed for class """
        return_str = f"[Rectangle] ({self.id}) "
        return_str += f"{self.x}/{self.y} - {self.width}/{self.height}"
        return return_str

    def update(self, *args):
        """ update values """
        ll = ["id", "width", "height", "x", "y"]
        for name, i in zip(ll, range(len(args))):
            setattr(self, name, args[i])
