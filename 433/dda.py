# This is a program to draw a line using the Digital Differential Analyzer Algorithm
import time


def dda(x0, y0, x1, y1):
    start = time.time()
    dx, dy = float(x1 - x0), float(y1 - y0)
    step = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    x_inc, y_inc, k = dx / step, dy / step, 1
    while k <= step:
        x0 += x_inc
        y0 += y_inc
        print("x{0} = {1}, y{2} = {3}".format(k, x0, k, y0))
        k += 1
    end = time.time()
    print("Seconds: ", end - start)


dda(1, 1, 645600, 765780)