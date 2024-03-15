#!/usr/bin/python3
if __name__ == '__main__':
    import calculator_1
    import sys
    args = sys.argv[:]

    if len(args) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>".format())
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if sys.argv[2] == "+":
        result = calculator_1.add(a, b)
        print("{} + {} = {}".format(a, b, result))
    elif sys.argv[2] == "-":
        result = calculator_1.sub(a, b)
        print("{} - {} = {}".format(a, b, result))
    elif sys.argv[2] == "*":
        result = calculator_1.mul(a, b)
        print("{} * {} = {}".format(a, b, result))
    elif sys.argv[2] == "/":
        result = calculator_1.div(a, b)
        print("{} / {} = {}".format(a, b, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
