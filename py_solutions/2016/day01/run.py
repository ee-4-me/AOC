import sys
sys.path.insert(0, '../../')
from helper.helper import getFile
import os
import math

def part1():
    contents = getFile(os.path.join(os.curdir, 'input.txt'))
    # neovim being dumb 
    if contents.endswith('\n'):
        contents = contents[:-1]
    contents = contents.split('\n')
    contents = contents[0].split(', ')

    x = 0
    y = 0
    dir = 0

    for line in contents:
        t = line[0]
        n = int(line[1:])

        if t == 'R':
            dir += 1
        else:
            dir -= 1
        if dir > 3:
            dir = 0
        if dir < 0:
            dir = 3

        if dir == 0:
            y -= n
        if dir == 1:
            x += n
        if dir == 2:
            y += n
        if dir == 3:
            x -= n

    return abs(x) + abs(y)

def part2():

    contents = getFile(os.path.join(os.curdir, 'input.txt'))
    # neovim being dumb 
    if contents.endswith('\n'):
        contents = contents[:-1]
    contents = contents.split('\n')
    contents = contents[0].split(', ')

    x = 0
    y = 0
    dir = 0

    h = {}
    h['0 0'] = 0

    for line in contents:
        t = line[0]
        n = int(line[1:])

        if t == 'R':
            dir += 1
        else:
            dir -= 1

        if dir > 3:
            dir = 0
        if dir < 0:
            dir = 3

        for i in range(n):
            if dir == 0:
                y -= 1
            if dir == 1:
                x += 1
            if dir == 2:
                y += 1
            if dir == 3:
                x -= 1

            key = f'{x} {y}'
            if key in h:
                return abs(x) + abs(y)
            h[key] = 0

print(f'part1: {part1()}')
print(f'part2: {part2()}')
