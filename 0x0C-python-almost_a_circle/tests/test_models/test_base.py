#!/usr/bin/python3
""" Test for Base class """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase(unittest.TestCase):
    """ Test Base Class """

    def test_id(self):
        """ test id case """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(None)
        self.assertEqual(b2.id, 2)
        b3 = Base(1)
        self.assertEqual(b3.id, 1)
        b4 = Base(1)
        self.assertEqual(b4.id, 1)
        b5 = Base()
        self.assertEqual(b5.id, 3)
        b6 = Base(-22)
        self.assertEqual(b6.id, -22)
        b7 = Base(0)
        self.assertEqual(b7.id, 0)

    def test_to_json_string(self):
        b1 = [{"id": 1, "width": 10}]
        b2 = [{"id": 3, "y": 8}, {"id": 20, "x": 3}]
        b3 = []
        b4 = None
        self.assertEqual(Base.to_json_string(b1), '[{"id": 1, "width": 10}]')
        self.assertEqual(Rectangle.to_json_string(b2), '[{"id": 3, "y": 8}, {"id": 20, "x": 3}]')
        self.assertEqual(Rectangle.to_json_string(b3), '[]')
        self.assertEqual(Base.to_json_string(b4), '[]')

    def test_save_to_file(self):
        b1 = Rectangle(2, 3, 4, 5)
        b2 = Rectangle(1, 2, 22, 11)
        b3 = Rectangle(6, 7, 0, 0)
        b4 = None






if __name__ == '__main__':
    print(Base)
    unittest.main()







