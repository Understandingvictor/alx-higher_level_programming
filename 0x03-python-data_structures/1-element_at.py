#!/usr/bin/python3
def element_at(my_list, idx):
    idx1 = idx + 1
  
    if idx < 0:
        return None
    if idx1 > len(my_list):
        return None
    else:
        for i in range(idx1):
            if i == idx:
                return my_list[i]
