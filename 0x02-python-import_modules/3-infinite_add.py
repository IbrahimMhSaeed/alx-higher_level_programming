#!/usr/bin/python3

import sys

if __name__ == '__main__':
    argv = sys.argv
    summ = 0

    for i, item in enumerate(argv):
        if i > 0:
            summ = summ + int(item)
    print(summ)
