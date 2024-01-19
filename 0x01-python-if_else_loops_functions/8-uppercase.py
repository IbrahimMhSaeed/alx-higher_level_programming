#!/usr/bin/python3
def uppercase(str):
    for c in str:
        asci = ord(c)
        if asci > 96 and asci < 123:
            asci = asci - 32
        print(f"{asci:c}", end='')
    print("")
