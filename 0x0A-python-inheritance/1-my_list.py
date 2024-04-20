#!/usr/bin/python3
""" module for myList class """


class MyList(list):
    """ my list class """
    def print_sorted(self):
        """ print sorted list """
        self.sort()
        print(self)

