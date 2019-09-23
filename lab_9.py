from random import randint

from tools import line_input


def task_1(n):
    arr = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i + j == n - 1:
                arr[i][j] = 1
            elif i + j > n - 1:
                arr[i][j] = 2

    return arr


def task_2(n, m):
    pass


def task_3(in_array, x):
    strings = 0

    for i in range(len(in_array)):
        elements = 0
        for j in range(len(in_array[i])):
            if x == in_array[i][j] % 10:
                elements += 1
        if 0 < elements < int(len(in_array) / 2):
            strings += 1
        
    return strings


def task_4(in_array, row, col):
    items = []

    for i in range(row + 1, col):
        items.append(in_array[i][i + 1: col])
    
    return items


if __name__ == '__main__':
    # print("n = ")
    # print(task_1(10))

    # print("n m = ")
    # print(task_2(line_input()[:2]))

    # print("n m x =")
    # n, m, x = line_input(int)[:3]
    # arr = []
    # print("enter array:")
    # for _ in range(n):
    #     print("line %i" % _)
    #     arr.append(line_input(int)[:n])
    # print('-' * 20)
    # print(task_3(arr, 1))

    # print("k s p = ")
    # k = line_input(int)[:3]
    # print array
    [print(item) for item in task_4([[randint(0, 50) for _ in range(15)] for _ in range(15)], 2, 9)]

    