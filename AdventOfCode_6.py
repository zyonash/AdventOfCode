def solve():
    which_santa = 0 # 0 is santa, 1 is robo santa
    x_coordinate_santa = 0
    y_coordinate_santa = 0
    x_coordinate_robo_santa = 0
    y_coordinate_robo_santa = 0
    houses_seen = 0
    house_map = {}
    temp_key = str(0)+ " and " + str(0)
    house_map[temp_key] = "Seen"
    f = open('input/AOC5_input.txt', 'r')
    while True:
        char = f.read(1)
        if which_santa == 0: # regular santa
            if char == '<':
                x_coordinate_santa -= 1
            if char == '>':
                x_coordinate_santa += 1
            if char == '^':
                y_coordinate_santa += 1
            if char == 'v':
                y_coordinate_santa -=1
            if not char:
                break
            temp_key = str(x_coordinate_santa)+ " and " + str(y_coordinate_santa)
            if not temp_key in house_map:
                house_map[temp_key] = "Seen"
                houses_seen += 1
        if which_santa == 1:
            if char == '<':
                x_coordinate_robo_santa -= 1
            if char == '>':
                x_coordinate_robo_santa += 1
            if char == '^':
                y_coordinate_robo_santa += 1
            if char == 'v':
                y_coordinate_robo_santa -=1
            if not char:
                break
            temp_key = str(x_coordinate_robo_santa)+ " and " + str(y_coordinate_robo_santa)
            if not temp_key in house_map:
                house_map[temp_key] = "Seen"
                houses_seen += 1

        if which_santa == 0:
            which_santa = 1
        elif which_santa == 1:
            which_santa = 0

    print houses_seen + 1 # + 1 for the starting location

solve()
