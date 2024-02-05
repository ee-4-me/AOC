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

    data = data.split('\n')

    grid = {}

    for index in range(len(data)):
        line = data[index]
        for j in range(len(line)):
            grid[(index, j)] = line[j]
        
    ans = ''

    for j in range(len(data[0])):
        h = {}
        for i in range(len(data)):
            c = grid[(i, j)]
            if c in h:
                h[c] += 1
            else:
                h[c] = 1

        mkey = ''
        mfreq = -1

        for k in h:
            if mkey == '':
                mkey = k
                mfreq = h[k]

            elif h[k] > mfreq:
                mfreq = h[k]
                mkey = k

        ans += mkey

    return ans 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    grid = {}

    for index in range(len(data)):
        line = data[index]
        for j in range(len(line)):
            grid[(index, j)] = line[j]
        
    ans = ''

    for j in range(len(data[0])):
        h = {}
        for i in range(len(data)):
            c = grid[(i, j)]
            if c in h:
                h[c] += 1
            else:
                h[c] = 1

        mkey = ''
        mfreq = -1

        for k in h:
            if mkey == '':
                mkey = k
                mfreq = h[k]

            elif h[k] < mfreq:
                mfreq = h[k]
                mkey = k

        ans += mkey

    return ans 

print(f'part1: {part1()}')
print(f'part2: {part2()}')
