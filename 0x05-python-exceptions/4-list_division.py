#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    ans = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
            ans.append(div)
        except TypeError:
            print("wrong type")
            ans.append(0)
        except IndexError:
            print("out of range")
            ans.append(0)
        except ZeroDivisionError:
            print("division by 0")
            ans.append(0)
        finally:
            div = 0

    return (ans)
