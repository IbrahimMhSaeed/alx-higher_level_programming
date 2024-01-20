#!/usr/bin/python3

if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys

    argv = sys.argv

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(argv[1])
    b = int(argv[3])
    ans = 0
    param = argv[2]

    if param == '+':
        ans = add(a, b)
    elif param == '-':
        ans = sub(a, b)
    elif param == '*':
        ans = mul(a, b)
    elif param == '/':
        ans = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, param, b, ans))
