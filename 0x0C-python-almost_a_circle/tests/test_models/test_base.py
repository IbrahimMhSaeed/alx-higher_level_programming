#!/usr/bin/python3
""" Test for Base class """
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """ Test Base Class """

    def test_id(self):
        """ test id case """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(55)
        self.assertEqual(b3.id, 55)
        b4 = Base()
        self.assertEqual(b4.id, 3)

if __name__ == '__main__':
    print(Base)
    unittest.main()
