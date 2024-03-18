#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    idx1 = idx + 1

    if idx < 0:
        return my_list
    if idx1 > len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
