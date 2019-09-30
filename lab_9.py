from random import randint

from tools import line_input, print_array


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

    for row in in_array:
        elements = 0
        for i in range(len(row)):
            if x == row[i] % 10:
                elements += 1
        if elements < int(len(row) / 2):
            strings += 1
        
    return strings


def task_4(in_array, row, col):
    items = []

    for i in range(row + 1, col):
        items.append(in_array[i][i + 1: col])
    
    return items


def task_5(in_array):
    return list(zip(*in_array[::-1]))


if __name__ == '__main__':
    print('Task 1')
    print("edge_size = ")
    print_array(task_1(int(input())))

    # print("n m = ")
    # print(task_2(line_input()[:2]))

    print('\nTask 3')
    print("[row_size col_size start_digit] =")
    row_size, col_size, start_digit = line_input(int)[:3]
    in_array = [[randint(0, 50) for _ in range(row_size)] for _ in range(col_size)]
    print('-' * 50 + '\nINPUT:')
    print_array(in_array)
    print('-' * 50 + '\n')
    print(task_3(in_array, start_digit))

    print('\nTask 4')
    print("[edge_size row col] = ")
    edge_size, row, col = line_input(int)[:3]
    in_array = [[randint(0, 50) for _ in range(edge_size)] for _ in range(edge_size)]
    print('-' * 50 + '\nINPUT:')
    print_array(in_array)
    print('-' * 50 + '\n')
    print_array(task_4(in_array, row, col))

    print('\nTask 5')
    in_array = [
        [1, 2, 3, 4, 5,],
        [6, 7, 8, 9, 10,],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]
    print_array(task_5(in_array))
    