import sys
sys.path.insert(0, '../../')
import os
import math
from helper.helper import getFile, mymap, myfilter, download_input

download_input(os.path.abspath(os.curdir), '')

def n(c):
    if c == c.upper():
        return ord(c) - 65 + 27
    return ord(c) - 97 + 1

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    sum = 0

    for index in range(len(data)):
        line = data[index]
        h1 = {}
        h2 = {}

        for i, c in enumerate(line):
            if i < len(line) / 2:
                h1[c] = 1
            else:
                h2[c] = 1

        for c in h1:
            if c in h2:
                sum += n(c)
                break
        
    return sum 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    sum = 0

    for index in range(0, len(data), 3):

        hs = [{}, {}, {}]

        for j in range(3):
            line = data[index + j]
            for i, c in enumerate(line):
                hs[j][c] = 1

        for c in hs[0]:
            if c in hs[1] and c in hs[2]:
                sum += n(c)
                break
        
    return sum 

print(f'part1: {part1()}')
print(f'part2: {part2()}')
