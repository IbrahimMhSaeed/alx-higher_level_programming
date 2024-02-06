#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        summ = a / b
    except ZeroDivisionError:
        summ = None
    finally:
        print("Inside result: {}".format(summ))
    return (summ)
