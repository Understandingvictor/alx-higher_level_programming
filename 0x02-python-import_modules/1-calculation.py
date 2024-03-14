#!/usr/bin/python3
import calculator_1 as func
a = 10
b = 5

print("{:d} + {:d} = {:d}".format(a, b, func.add(a, b)))
print("{:d} - {:d} = {:d}".format(a, b, func.sub(a, b)))
print("{:d} * {:d} = {:d}".format(a, b, func.mul(a, b)))
print("{:d} / {:d} = {:d}".format(a, b, func.div(a, b)))
