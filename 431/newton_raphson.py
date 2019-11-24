import math


def fx(x):
    return math.pow(x, 3) - 2 * math.pow(x, 2) + x - 3


def fpx(x):
    return 3 * math.pow(x, 2) - 4 * x + 1


def regula_falsi(c0):
    c = round(c0 - fx(c0) / fpx(c0), 4)
    error = abs(c - c0)
    print("x = {0} and error = {1}".format(c, error))
    if error > 0.03:
        regula_falsi(c)


regula_falsi(4)