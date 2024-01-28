#!/usr/bin/python3


def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return (0)
    weight = 0
    summ = 0
    for t in my_list:
        val, wei = t
        summ = summ + (val  * wei)
        weight = weight + wei
    ans = float(summ) / weight
    return (ans)
