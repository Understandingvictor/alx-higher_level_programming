#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list2 = []
    idx1 = idx + 1

    if idx < 0:
        return my_list
    if idx1 > len(my_list):
        return my_list
    else:
        for i in my_list:
            my_list2.append(i)

    my_list2[idx] = element
    return (my_list2)
