

def task_1(in_file_name, out_file_name, in_string):
    with open(in_file_name, 'r') as in_file:
        with open(out_file_name, 'a+') as out_file:
            data = in_file.read() + in_string
            out_file.write(data)


def task_2(in_file_name, out_file_name, del_str_number):
    with open(in_file_name, 'r') as in_file:
        with open(out_file_name, 'w+') as out_file:
            lines = in_file.readlines().pop(del_str_number)
            out_file.write(''.join(lines))


def task_3(in_file_name, out_file_name, start_symbol):
    with open(in_file_name, 'r') as in_file:        
        with open(out_file_name, 'w+') as out_file:
            i = 0
            text = in_file.read()
            while i < len(text):
                word = ''
                j = i
                while j < len(text):
                    if text[i].isalpha():
                        word += text[i]
                    i += 1

            
    

if __name__ == '__main__':
    # print(task_1('lab_10_data/input_1.txt', 'lab_10_data/output_1.txt', 'sihuyfuyergfueyr'))

    # print(task_2('lab_10_data/input_2.txt', 'lab_10_data/output_2.txt', 5))
    print(task_3('lab_10_data/input_3.txt', 'lab_10_data/output_3.txt', 'ы'))
