#!/usr/bin/python3


def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string == None:
        return (0)

    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    sum_rom = 0
    lenn = len(roman_string) - 1
    prev = 0

    for i in range(lenn, -1, -1):
        curr = rom_num[roman_string[i]]
        if prev > curr:
            sum_rom = sum_rom - curr
        else:
            sum_rom = sum_rom + curr
        prev = curr
    return (sum_rom)
