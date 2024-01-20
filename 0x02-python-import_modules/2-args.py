#!/usr/bin/python3

import sys

if __name__ == '__main__':
    argv = sys.argv
    llen = len(argv)

    if llen == 2:
        print("1 argument:")
    elif llen == 1:
        print("0 arguments.")
    else:
        print("{} arguments:".format(len(argv) - 1))

    for i, item in enumerate(argv):
        if i > 0:
            print("{}: {}".format(i, item))
