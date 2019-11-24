import math


def fx(x):
    return x - math.cos(x)


def bisection(a, b, c0):
    c = (a + b) / 2
    error = abs(c - c0) / abs(c)
    print("[a, b] = [{0}, {1}], c = {2} and error = {3}".format(a, b, c, error))
    if error > 0.2:
        if fx(a) * fx(c) < 0:
            bisection(a, c, c)
        else:
            bisection(c, b, c)


bisection(0, 1, 1)