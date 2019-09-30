
def line_input(to_type):
    data = input().split()
    
    return [to_type(item) for item in data]


def print_array(array):
    for row in array:
        print('\t'.join([str(element) for element in row]))
