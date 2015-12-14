def solve():
    counter = 0
    position = 0
    f = open('input/AOC1_input.txt', 'r')
    while True:
        direction = f.read(1)
        if direction == '(':
            position = position + 1
            counter = counter + 1
        elif direction == ')':
            position = position - 1
            counter = counter + 1
        if position == -1:
            print "Done stepping! The position of the character is " + str(counter)
            break

solve()