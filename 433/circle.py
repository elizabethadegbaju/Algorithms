# This is a program to implement the Mid-Point Circle Drawing Algorithm
# Written by Adeotun Adegbaju 16CG021378

def circle(r):
    y0, x0 = r, 0
    y1, x1 = y0, x0
    pk = 1 - r
    x_values, y_values = [], []

    while y1 > x1:
        x_values.append(x1)
        y_values.append(y1)
        if pk > 0:
            y0, x0 = y1, x1
            x1 = x0 + 1
            y1 = y0 - 1
        else:
            y0, x0 = y1, x1
            x1 = x0 + 1
            y1 = y0
        pk = pk + 2 * (x0 + 1) + (pow(y1, 2) - pow(y0, 2)) - (y1 - y0) + 1
    y_reverse, x_reverse = y_values.copy(), x_values.copy()
    y_reverse.reverse()
    x_reverse.reverse()
    x_values = x_values + y_reverse
    y_values = y_values + x_reverse

    # Printing points to draw the circle
    i = 0
    print("\nQuarter 1")
    while i < len(x_values):
        print("(xk, yk) = ({0},{1})".format(x_values[i], y_values[i]))
        i += 1

    i = 0
    print("\nQuarter 2")
    while i < len(x_values):
        print("(xk, yk) = ({0},{1})".format(-x_values[i], y_values[i]))
        i += 1

    i = 0
    print("\nQuarter 3")
    while i < len(x_values):
        print("(xk, yk) = ({0},{1})".format(-x_values[i], -y_values[i]))
        i += 1

    i = 0
    print("\nQuarter 4")
    while i < len(x_values):
        print("(xk, yk) = ({0},{1})".format(x_values[i], -y_values[i]))
        i += 1


circle(8)