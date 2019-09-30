from tools import line_input


def task_1(a, b, c, d):
    return (max(a, b, c), max(a, b, d), max(a, c, d))


def count_item(index):
    return (index + 1) / (index + 2)


def task_2(max):
    result = 0
    items = 0
    
    i = 1
    while True:
        item = count_item(i)
        if item < max:
            items += 1
            result += item
        else:
            break

        i += 1

    return result, items 


if __name__ == '__main__':
    # print("a b c d = ")
    # print("max(a, b, c)=%f\nmax(a, b, d)=%f\nmax(a, c, d)=%f" % task_1(*line_input(float)[:4]))
    print('Task 1')
    a, b, c, d = 12.0123, 123.54, -98.150, 11
    print('-' * 20, "INPUT:", sep='\n')
    print("a = ", a, ", b = ", b, ", c = ", c, ", d = ", d)
    print('-' * 20)
    print("max(a, b, c)=%f\nmax(a, b, d)=%f\nmax(a, c, d)=%f" % task_1(a, b, c, d))

    print('\nTask 2')
    print("epsilon = ")
    print("Sum: %f\nNumbers: %i" % task_2(float(input())))
