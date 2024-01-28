#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    s_dict = sorted(a_dictionary)
    for key in s_dict:
        print(f"{key}: {a_dictionary[key]}")
