def solve():
    counter = 0
    f = open('input/AOC1_input.txt', 'r')
    while True:
        direction = f.read(1)
        if direction == '(':
            counter = counter + 1
        elif direction == ')':
            counter = counter - 1
        if not direction:
            print "Done stepping! He should be on floor " + str(counter)
            break

solve()