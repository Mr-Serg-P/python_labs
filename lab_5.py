from tools import line_input

def task_1(temp_start, temp_stop):
    table = [('°C', '°F',),]

    while temp_start <= temp_stop:
        temp_f = 1.8 * temp_start + 32
        table.append((temp_start, temp_f))
        temp_start += 1
    
    return table

def task_2(n, digits):
    
    armstrong_sum = 0
    while n:
        armstrong_sum += (n % 10)**3
        n = int(n / 10)

    return armstrong_sum

def task_3(max):
    i = 1
    
    result = 0
    items = 0
    while True:
        item = (i + 1) / (i + 2)
        if item < max:
            items += 1
            result += item
        else:
            break

        i += 1

    return result, items    


if __name__ == '__main__':
    print("Task 1")
    print("a b = ")
    a, b = line_input(float)[:2]
    for row in task_1(a, b):
        print(*row, sep='\t\t')
    
    print("\nTask 2")
    print("n = ")   # 153 - Armstrong's number
    n = input()
    print("%s is Armstrong's number" % n if task_2(int(n), len(n)) == int(n) else "%s Isn't Armstrong's number" % n)

    print("\nTask 3")
    print(*task_3(float(input())))
