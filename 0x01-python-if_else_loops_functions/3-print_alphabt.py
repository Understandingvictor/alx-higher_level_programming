#!/usr/bin/python3
for i in range(97, 123):
    alphabets = chr(i)

    if alphabets == "q" or alphabets == "e":
        continue
    print("{}".format(alphabets), end="")
