
def line_input(to_type):
    data = input().split()
    
    return [to_type(item) for item in data]
