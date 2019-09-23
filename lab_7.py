

def task_1(in_str):
    if not len(in_str) & 1:
        return in_str[0] + in_str[1:].replace(in_str[0], '')

    return in_str


def task_2(in_str):
    in_str = in_str.split(' ')

    for i in range(len(in_str)):
        vowels = 0
        print(i, len(in_str))
        for letter in in_str[i]:
            if letter in ('а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'):
                vowels += 1
        
        if vowels > len(in_str[i]) - vowels:
            in_str[i] = '*' + in_str[i]
    
    return ' '.join(in_str)

if __name__ == '__main__':
    print("Enter string")
    print(task_1(input()))

    print("Enter string")
    print(task_2(input()))
    