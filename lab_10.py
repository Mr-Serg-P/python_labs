

def task_1(in_file_name, out_file_name, in_string):
    with open(in_file_name, 'r') as in_file:
        with open(out_file_name, 'a+') as out_file:
            data = in_file.read() + in_string
            out_file.write(data)


def task_2(in_file_name, out_file_name, del_str_number):
    with open(in_file_name, 'r') as in_file:
        with open(out_file_name, 'w+') as out_file:
            lines = map(lambda line: line[del_str_number:len(line) - 1], in_file.readlines())
            out_file.write('\n'.join(list(lines)))


def task_3(in_file_name, out_file_name, start_symbol):
    with open(in_file_name, 'r', encoding='utf-8') as in_file:        
        words = in_file.read().lower().split()
    with open(out_file_name, 'w+', encoding='utf-8') as out_file:
        start_symbol = start_symbol.lower()
        for word in words:
            if word[0] == start_symbol:
                out_file.write(word + ' ')

            
def task_4(in_file_name, out_file_name):
    with open(in_file_name, 'r') as in_file:
        numbers = list(map(lambda x: x, in_file.read().split()))
    
    with open(out_file_name, 'w+') as out_file:
        for number in numbers:
            if float(number) > int(float(number)):
                out_file.write(number + ' ')


if __name__ == '__main__':
    print(task_1('lab_10_data/input_1.txt', 'lab_10_data/output_1.txt', 'sihuyfuyergfueyr'))

    print(task_2('lab_10_data/input_2.txt', 'lab_10_data/output_2.txt', 20))
    
    print(task_3('lab_10_data/input_3.txt', 'lab_10_data/output_3.txt', 'Г'))

    print(task_4('lab_10_data/input_4.txt', 'lab_10_data/output_4.txt'))
