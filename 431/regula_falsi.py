import math


def fx(x):
    return math.pow(x, 2) - 1


def regula_falsi(a, b, c0):
    c = round(b - (fx(b) * (a - b)) / (fx(a) - fx(b)), 4)
    error = abs(c - c0) / abs(c)
    print("[a, b] = [{0}, {1}], c = {2} and error = {3}".format(a, b, c, error))
    if error > 0.2:
        if fx(a) * fx(c) < 0:
            regula_falsi(a, c, c)
        else:
            regula_falsi(c, b, c)


regula_falsi(0, 1.5, 0)