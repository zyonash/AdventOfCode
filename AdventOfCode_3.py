import string

def solve():
    total_square_feet = 0
    f = open('input/AOC3_input.txt', 'r')
    while True:
        line = f.readline()
        box_dims = string.split(line,"x",2)
        total_square_feet = total_square_feet + calculate(box_dims)
        if not line:
            print total_square_feet
            break

def calculate(box_dims):
    length = 0
    width = 0
    height = 0
    counter = 0 # Counter 0 means length (l), counter 1 means width (w), counter 2 means height (h)
    smallest_dim = 0
    for dim in box_dims:
        if not dim:
            break
        dim = int(dim)
        if counter == 0:
            length = dim
        if counter == 1:
            width = dim
        if counter == 2:
            height = dim
        counter = counter + 1
        if length > 0 and width > 0 and height > 0:
            smallest_dim = min((length*width),(width*height),(height*length))

    final_calc = (2*length*width) + (2*width*height) + (2*height*length) + smallest_dim
    return final_calc

solve()
