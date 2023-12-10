import sys
sys.path.insert(0, '../../')
import os
import math
import copy
from helper.helper import getFile, mymap, myfilter, download_input, hash_string, hashes_equal

download_input(os.path.abspath(os.curdir))

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')
    data = [int(x) for x in data]

    i = 0
    s = 0
    while True:
        ii = i
        i += data[i]
        data[ii] += 1
        s += 1
        if i < 0 or i >= len(data):
            return s

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')
    data = [int(x) for x in data]

    i = 0
    s = 0
    while True:
        ii = i
        i += data[i]
        if data[ii] >= 3:
            data[ii] -= 1
        else:
            data[ii] += 1
        s += 1
        if i < 0 or i >= len(data):
            return s

print(f'part1: {part1()}')
print(f'part2: {part2()}')
