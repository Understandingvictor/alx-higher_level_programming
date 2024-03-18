#!/usr/bin/env python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        k = 0
        for j in i:
            k += 1
            print("{:d}{}".format(j, "" if k == 3 else " "), end="")
        print()
