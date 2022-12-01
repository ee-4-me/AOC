import sys
sys.path.insert(0, '../../')
import os
import math
from helper.helper import getFile

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')
    data = data[0]

    sum = 0

    x = 0
    y = 0

    h = {}
    h['0 0'] = 1

    for index in range(len(data)):
        c = data[index]
        if c == '^':
            y -= 1
        if c == 'v':
            y += 1
        if c == '<':
            x -= 1
        if c == '>':
            x += 1
         
        k = f'{x} {y}'
        h[k] = 1

    sum = 0
    for k in h:
        sum += 1
    return sum 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')
    data = data[0]

    sum = 0

    x = [0, 0]
    y = [0, 0]

    h = {}
    h['0 0'] = 1

    for index in range(len(data)):
        i = index % 2
        c = data[index]
        if c == '^':
            y[i] -= 1
        if c == 'v':
            y[i] += 1
        if c == '<':
            x[i] -= 1
        if c == '>':
            x[i] += 1
         
        k = f'{x[i]} {y[i]}'
        h[k] = 1

    sum = 0
    for k in h:
        sum += 1
    return sum 

print(f'part1: {part1()}')
print(f'part2: {part2()}')
