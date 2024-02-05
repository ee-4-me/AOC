import sys
sys.path.insert(0, '../../')
import os
import math
import copy
from itertools import permutations
from helper.helper import getFile, mymap, myfilter, download_input, hash_string, hashes_equal, key, key3, UP, DOWN, LEFT, RIGHT, dUP, dRIGHT, dDOWN, dLEFT

download_input(os.path.abspath(os.curdir))

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\t')

    h = {}

    data = [int(x) for x in data]

    count = 0

    while True:
        s = ', '.join([str(x) for x in data])
        if s in h:
            break

        h[s] = 0

        big = -1
        big_ind = -1

        for i in range(len(data)):
            d = data[i]
            if d > big:
                big = d
                big_ind = i

        data[big_ind] = 0

        while big > 0:
            big_ind = (big_ind + 1) % len(data)
            data[big_ind] += 1
            big -= 1

        count += 1

    return count

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\t')

    h = {}

    data = [int(x) for x in data]

    count = 0

    while True:
        s = ', '.join([str(x) for x in data])
        if s in h:
            if h[s] == 1:
                break
            count += 1
            h[s] += 1
        else:
            h[s] = 0

        big = -1
        big_ind = -1

        for i in range(len(data)):
            d = data[i]
            if d > big:
                big = d
                big_ind = i

        data[big_ind] = 0

        while big > 0:
            big_ind = (big_ind + 1) % len(data)
            data[big_ind] += 1
            big -= 1

    return count


print(f'part1: {part1()}')
print(f'part2: {part2()}')
