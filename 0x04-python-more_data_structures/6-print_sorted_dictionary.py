#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortedKeys = sorted(a_dictionary.keys())
    for i in sortedKeys:
        print(f"{i}: {a_dictionary[i]}")
