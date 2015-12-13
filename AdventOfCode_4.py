import string

def solve():
    total_ribbon_feet = 0
    f = open('AOC3_input.txt', 'r')
    while True:
        line = f.readline()
        box_dims = string.split(line,"x",2)
        total_ribbon_feet = total_ribbon_feet + calculate(box_dims)
        if not line:
            print total_ribbon_feet
            break

def calculate(box_dims):
    length = 0
    width = 0
    height = 0
    counter = 0 # Counter 0 means length (l), counter 1 means width (w), counter 2 means height (h)
    largest_dim = 0
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
            largest_dim = max(width,length,height)



    shortest_perim = []
    if length != largest_dim:
        shortest_perim.append(length)
    if width != largest_dim:
        shortest_perim.append(width)
    if height != largest_dim:
        shortest_perim.append(height)

    if len(shortest_perim) == 1:
        shortest_perim.append(largest_dim)
    if len(shortest_perim) == 0:
        shortest_perim.append(width)
        shortest_perim.append(height)

    final_calc = (shortest_perim[0]*2) + (shortest_perim[1]*2) + (width*length*height)
    return final_calc

solve()