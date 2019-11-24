# This is a program to draw a line using the Bresenham Algorithm
import time


def bresenham(x0, y0, x1, y1):
    start = time.time()
    # dx, dy, k, final, x1, y1 = float(x1 - x0), float(y1 - y0), 0, y1, x0, y0       --python 2.x and earlier versions
    dx, dy, k, final, x1, y1 = x1 - x0, y1 - y0, 0, y1, x0, y0
    p, m = 2 * dx - dy, dy / dx
    while y1 < final:
        if k != 0:
            p = p + 2 * dx - 2 * dy * (x1 - x0)
            m = dy / dx
        if p >= 0:
            x0 = x1
            x1 += 1
            y1 += 1
            print("x{0} = {1}, y{2} = {3}, p{4} = {5}".format(k, x1, k, y1, k, p))
            k += 1
        elif m < 1:
            x0 = x1
            x1 += 1
            print("x{0} = {1}, y{2} = {3}, p{4} = {5}".format(k, x1, k, y1, k, p))
            k += 1
        elif m > 1:
            x0 = x1
            y1 += 1
            print("x{0} = {1}, y{2} = {3}, p{4} = {5}".format(k, x1, k, y1, k, p))
            k += 1
    end = time.time()
    print("Seconds: ", end - start)


bresenham(1, 1, 645600, 765780)