# This is a program to implement the Mid-Point Ellipse Drawing Algorithm
# Written be ELizabeth Adeotun Adegbaju 16CG021378

def ellipse(rx, ry):
    # Computing values for region 1
    y0, x0 = ry, 0
    y1, x1 = y0, x0
    p1k = (ry ** 2) + ((rx ** 2) / 4) - (ry * (rx ** 2))
    x_values, y_values = [], []

    while (2 * (ry ** 2) * x1 < 2 * (rx ** 2) * y1):
        if p1k < 0:
            y0, x0 = y1, x1
            x1 = x0 + 1
            y1 = y0
        else:
            y0, x0 = y1, x1
            x1 = x0 + 1
            y1 = y0 - 1
        p1k = p1k + (ry ** 2) + 2 * (x0 + 1) * (ry ** 2) + (rx ** 2) * ((y1 ** 2) - (y0 ** 2)) - (rx ** 2) * (y1 - y0)
        x_values.append(x1)
        y_values.append(y1)

    # Computing values for region 2
    y0, x0 = y_values[-1], x_values[-1]
    y1, x1 = y0, x0
    p2k = ((x0 + 1 / 2) ** 2) * (ry ** 2) + ((y0 - 1) ** 2) * (rx ** 2) - (rx ** 2) * (ry ** 2)

    while (x1 != rx & y1 != ry):
        if p2k < 0:
            y0, x0 = y1, x1
            x1 = x0 + 1
            y1 = y0 - 1
        else:
            y0, x0 = y1, x1
            x1 = x0
            y1 = y0 - 1
        p2k = p2k + (rx ** 2) + 2 * (y0 - 1) * (rx ** 2) + (ry ** 2) * ((x1 ** 2) - (x0 ** 2)) - (ry ** 2) * (
                x1 - x0)
        x_values.append(x1)
        y_values.append(y1)

    # Printing points to draw the ellipse
    x_values.pop(-1)
    y_values.pop(-1)
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


ellipse(8, 6)