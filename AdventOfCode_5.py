def solve():
    x_coordinate = 0
    y_coordinate = 0
    houses_seen = 0
    house_map = {}
    f = open('input/AOC5_input.txt', 'r')
    while True:
        char = f.read(1)
        if char == '<':
            x_coordinate -= 1
        if char == '>':
            x_coordinate += 1
        if char == '^':
            y_coordinate += 1
        if char == 'v':
            y_coordinate -=1
        if not char:
            break
        temp_key = str(x_coordinate)+ " and " + str(y_coordinate)
        if not temp_key in house_map:
            house_map[temp_key] = "Seen"
            houses_seen += 1

    print houses_seen + 1 # + 1 for the starting location

solve()
