#!/usr/bin/python3
def remove_char_at(str, n):
    ans = ''
    for i, item in enumerate(str):
        if n == i:
            continue
        ans = ans + item

    return ans
