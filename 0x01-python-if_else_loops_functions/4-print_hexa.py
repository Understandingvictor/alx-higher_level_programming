#!/usr/bin/python3
for i in range(0, 99):
    if i < 10:
        print("{} = 0x{}".format(i, i))
    if i >= 10:
        print("{} = 0x{:x}".format(i, i))
