#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None

    filteredList = []
    keys = list(a_dictionary.values())

    for i in keys:
        if type(i) == int:
            filteredList.append(i)

    if filteredList == []:
        return None

    maxNum = max(filteredList)
    maxNumidx = keys.index(maxNum)

    count = 0
    for k, v in a_dictionary.items():
        if count == maxNumidx:
            return k
        count += 1
