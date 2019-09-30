from math import sin

from tools import line_input


def task_1(n):
    y = 0
    for i in range(1, n + 1):

        denominator = 0
        for j in range(1, i + 1):
            denominator += sin(j)

        y += (1 + i) / denominator

    return y


def task_2(n, numbers):
    mul = None
    for i in range(len(nums)):
        if i + 1 < nums[i] < i:
            mul = nums[i] if mul is None else mul * nums[i]

    return 1 / mul


def task_3(n):
    is_simple = True
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True


if __name__ == '__main__':
    print("Task 1")
    print("n = ")
    print("Result: ", task_1(int(input())))

    # print("\nTask 2")
    # print("n = ")
    # n = int(input())
    # print("Enter numbers divided with space: ")
    # nums = line_input(float)
    # print(task_2(n, nums))

    print("\nTask 3 ")
    print("n = ")
    n = int(input())
    if task_3(n):
        print(n, "is simple")
    else:
        print(n, "is not simple")
