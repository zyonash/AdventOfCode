import hashlib


def solve():
    incremental = 1   # This program has been run up to this incremental point.  Starting here.
    f = open('input/AOC7_input.txt','r')
    orig_secret_key = f.readline()

    while True:
        flag = 0
        secret_key = orig_secret_key + str(incremental)
        m = hashlib.md5()
        m.update(secret_key)
        md5 = m.hexdigest()
        for i in range(6):
            if md5[i] != str(0):
                incremental += 1
                break
            else:
                flag += 1

        if flag == 6:
            print "Got it: " + str(incremental)
            print md5
            break

solve()