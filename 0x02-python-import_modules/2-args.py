#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    j = 1
    length = len(sys.argv)
    print("{} {}:".format(length, "arguments" if length > 1 else "argument"))
    for i in sys.argv:
        print("{:d}: {:d}".format(j, i))
        j += 1
