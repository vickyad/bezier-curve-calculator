def get_point(p1, p2, t):
    return p1 + (p2 - p1) * t


def calculate_coordinate(x, y, num):
    # Caso mais simples: curvas de grau 2
    if num == 3:
        x0 = get_point(x[0], x[1], i / iterations)
        y0 = get_point(y[0], y[1], i / iterations)
        x1 = get_point(x[1], x[2], i / iterations)
        y1 = get_point(y[1], y[2], i / iterations)
        bezier_curve_x.append(get_point(x0, x1, i / iterations))
        bezier_curve_y.append(get_point(y0, y1, i / iterations))
    else:
        x_next = []
        y_next = []
        for j in range(num - 1):
            x_next.append(get_point(x[j], x[j + 1], i / iterations))
            y_next.append(get_point(y[j], y[j + 1], i / iterations))
        calculate_coordinate(x_next, y_next, num - 1)
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    iterations = 20

    # Control points
    control_points_x = [-0.6, -0.2, 0.5, 0.9]
    control_points_y = [-0.3, 0.9, -0.4, 0.2]

    # Bezier Curve points
    bezier_curve_x = []
    bezier_curve_y = []

    for i in range(iterations + 1):
        calculate_coordinate(control_points_x, control_points_y, len(control_points_x))
        print(bezier_curve_x)
        print(bezier_curve_y)

    print(control_points_x)
    print(control_points_y)
    print(bezier_curve_x)
    print(bezier_curve_y)
