from math import sqrt, sin, cos, exp

from tools import line_input


if __name__ == '__main__':
    print("Lab 3")
    print('*' * 15, " Task 1 ", '*' * 15)

    print("x a = ")
    x, a = line_input(float)[:2]

    if x > a:
        y = x * sqrt(x - a)
    elif x == a:
        y = x / sin(a * x)
    else:
        y = exp(-a * x) * cos(a * x)

    print("y = ", y, '\n')

# --------------------------------------------

    print('*' * 15, " Task 2 ", '*' * 15)

    print("N = ")
    years = int(input())

    if 9 < years < 21:
        suffics = 'лет'
    elif years % 10 == 1:
        suffics = 'год'
    elif 0 < years % 10 < 5:
        suffics = 'года'
    else:
        suffics = 'лет'

    print(years, suffics)
