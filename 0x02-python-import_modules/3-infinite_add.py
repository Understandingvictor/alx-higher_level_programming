#!/usr/bin/python3
import sys
arguments = sys.argv[1:]

if __name__ == '__main__':
    sum = 0
    for i in arguments:
        i = int(i)
        sum += i
    print("{}".format(sum))
