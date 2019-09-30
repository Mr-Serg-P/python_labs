from math import sqrt, sin, cos, exp

from tools import line_input


def task_1(x, a):
    if x > a:
        y = x * sqrt(x - a)
    elif x == a:
        y = x / sin(a * x)
    else:
        y = exp(-a * x) * cos(a * x)

    return y


def task_2(years):
    if 9 < years < 21:
        suffics = 'лет'
    elif years % 10 == 1:
        suffics = 'год'
    elif 0 < years % 10 < 5:
        suffics = 'года'
    else:
        suffics = 'лет'
    
    return suffics


if __name__ == '__main__':
    print("Task 1 ")
    print("[x a] = ")
    x, a = line_input(float)[:2]
    print("y = ", task_1(x, a), '\n')

    print("\nTask 2")
    print("years = ")
    years = int(input())
    print(years, task_2(years))
