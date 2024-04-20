#!/usr/bin/python3
""" module for myList class """


class MyList(list):
    """ my list class """
    def print_sorted(self):
        """ print sorted list """
        ll = [x for x in self]
        ll.sort()
        print(ll)

