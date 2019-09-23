from math import sin

from tools import line_input


if __name__ == '__main__':
    print("Lab 4")
    print('*' * 15, " Task 1 ", '*' * 15)

    print("N = ")
    n = int(input())

    y = 0
    for i in range(1, n + 1):

        denominator = 0
        for j in range(1, i + 1):
            denominator += sin(j)

        y += (1 + i) / denominator

    print("Result: ", y)

    # ----------------------------------

    print('\n', '*' * 15, " Task 2 ", '*' * 15)

    print("n = ")
    n = int(input())
    print("Enter numbers divided with space: ")
    nums = line_input(float)

    mul = None
    for i in range(len(nums)):
        if i + 1 < nums[i] < i:
            mul = nums[i] if mul is None else mul * nums[i]

    print(1 / mul)

    # ----------------------------------

    print('\n', '*' * 15, " Task 3 ", '*' * 15)

    print("n = ")
    n = int(input())

    is_simple = True
    for i in range(2, n):
        if n % i == 0:
            is_simple = False
            break

    if is_simple:
        print(n, "is simple")
    else:
        print(n, "is not simple")
