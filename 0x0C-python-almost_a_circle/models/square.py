#!/usr/bin/python3
""" Square Module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square Class """

    def __init__(self, size, x=0, y=0, id=None):
        """ init function """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ string printing function """
        rt_str = f"[Square] ({self.id}) "
        rt_str += f"{self.x}/{self.y} - {self.width}"
        return rt_str

    @property
    def size(self):
        """ getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """ setter for size """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update values """
        if args:
            if len(args) != 0:
                ll = ["id", "size", "x", "y"]
                for name, i in zip(ll, range(len(args))):
                    setattr(self, name, args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ to dictionary function """
        dd = {}
        for key, value in self.__dict__.items():
            if key == "width" or key == "height":
                dd["size"] = self.__dict__[key]
            else:
                dd[key] = self.__dict__[key]
        return dd
