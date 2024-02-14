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

    data = data.split('\n\n')

    sum = 0

    for index in range(len(data)):
        group = data[index]
        h = {}

        for line in group.split('\n'):
            for c in line:
                if c in h:
                    h[c] += 1
                else:
                    h[c] = 1

        for k in h:
            sum += 1

    return sum 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n\n')

    sum = 0

    for index in range(len(data)):
        group = data[index]
        h = {}

        for line in group.split('\n'):
            for c in line:
                if c in h:
                    h[c] += 1
                else:
                    h[c] = 1

        people = len(group.split('\n'))

        for k in h:
            if h[k] == people:
                sum += 1

    return sum 

print(f'part1: {part1()}')
print(f'part2: {part2()}')
