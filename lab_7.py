

def task_1(in_str):
    if not len(in_str) & 1:
        return in_str[0] + in_str[1:].replace(in_str[0], '')

    return in_str


def task_2(in_str):
    in_str = in_str.split(' ')
    words = 0
    for i in range(len(in_str)):
        vowels = 0
        for letter in in_str[i]:
            if letter in ('а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'):
                vowels += 1
        
        if vowels > len(in_str[i]) - vowels:
            in_str[i] = '*' + in_str[i]
            words += 1
    
    return (' '.join(in_str), words)

if __name__ == '__main__':
    # print("Enter string")
    # print(task_1(input()))
    print('Task 1')
    s = "строка с четным количеством символов"
    print('-' * 20, 'INPUT:', s, '-' * 20, task_1(s), sep='\n')
    print()

    print('\nTask 2')
    # print("Enter string")
    # print(task_2(input()))
    s = "гусь артишок чихуахуа банан"
    print('-' * 20, 'INPUT:', s, '-' * 20, *task_2(s), sep='\n')
    print()
    