from math import sin, exp

from tools import line_input


def count(x, y):
    a = ((1 + y) * (x + y**2) / exp(-x - 2)) + 1 / y
    b = 1 + abs(y - x) + (y - x)**2 / 2 + abs(y - x)**3 / (x * (y - 10))
    c = (x + 10 + y)**2 * ((sin(x) + sin(x + 5)**2) / abs(x - y -5))

    return (a, b, c)


if __name__ == '__main__':
    print('x y = ')
    x, y = line_input(float)[:2]

    result = count(x, y)

    print("1. ", [int(item) for item in result])
    print("2. ", result)

    print('\nh m s = ')
    h, m, s = line_input(float)[:3]

    result = (360 / 12) * h + (30 / 60) * m + (0.5 / 60) * s

    print(result % 360)
