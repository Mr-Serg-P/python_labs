from random import randint, uniform

from tools import line_input


def count_zeros(num):
    zeros = 1 if num == 0 else 0 
    while num:
        if not num % 10:
            zeros += 1

        num = int(num / 10)
    
    return zeros


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def task_1(arr):
    def sum_of_elements():
        result = 0
        for item in arr:
            if (not item & 1) and (count_zeros(item) == 2):
                result += item

        return result

    def max_not_prime():
        max_prime = None

        for item in arr:
            if not is_prime(item) and (not max_prime or item > max_prime):
                max_prime = item

        return max_prime

    return (sum_of_elements(), max_not_prime())


def selection_sort(iterable, start=None, stop=None, descend=False):
    cmp = (lambda x, y: x > y) if descend else (lambda x, y: x < y)
    start, stop = start if start else 1, stop if stop else len(iterable) - 1

    for i in range(stop, start, -1):
        for j in range(start, i):
            if cmp(iterable[i], iterable[j]):
                iterable[i], iterable[j] = iterable[j], iterable[i]

    return iterable


def task_2(arr):
    start = stop = -1
    for i in range(len(arr)):
        num_str = str(arr[i])

        if (num_str.find('.') != -1) and (num_str[num_str.find('.') + 1] == '8'):
            start = i + 1 if start == -1 else start
            stop = i
    
    return selection_sort(arr, start, stop, True)

    
if __name__ == "__main__":
    print('Task 1')
    print("Array length:")
    arr = [randint(150, 200) for _ in range(int(input()))]
    print('-' * 20, 'INPUT:', arr, '-' * 20, sep='\n')
    print("Sum of even numbers with 2 zeros: %i\nMax not prime: %i" % task_1(arr))

    print('\nTask 2')
    # print("start stop array_length = ")
    # start, stop, arr_len = line_input(float)[:3]
    # arr = [uniform(start, stop) for _ in range(int(arr_len))]
    arr = [0.2, 0.8, 0.5, -0.11, 10.1, 0.001, 0.98, 0.801, -1000.1]
    print('-' * 20, 'INPUT:', arr, '-' * 20, sep='\n')
    print(task_2(arr))
