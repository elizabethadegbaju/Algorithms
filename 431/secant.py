import math


def fx(x):
    return math.pow(x, 2) - 2 * x + 0.5


def secant(x0, x1):
    c = round(x1 - (fx(x1) * (x1 - x0) / (fx(x1) - fx(x0))), 4)
    error = abs(c - x1)
    print("x = {0} and error = {1}".format(c, error))
    if error > 0.03:
        secant(c, x1)


secant(0, 1)
