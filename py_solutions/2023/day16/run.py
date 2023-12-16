import sys
sys.path.insert(0, '../../')
import os
import math
import copy
from itertools import permutations
from helper.helper import getFile, key3, mymap, myfilter, download_input, hash_string, hashes_equal, key

download_input(os.path.abspath(os.curdir))

# 00:33:58   1900, really happy with this
def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    grid = []

    for index in range(len(data)):
        line = data[index]
        grid.append([c for c in line])
        

    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3

    mRIGHT = [0, 1]
    mDOWN = [1, 0]
    mLEFT = [0, -1]
    mUP = [-1, 0]

    dir_map = {
        RIGHT: {
            '.': [mRIGHT],
            '-': [mRIGHT],
            '\\': [mDOWN],
            '/': [mUP],
            '|': [mUP, mDOWN],
        },
        DOWN: {
            '.': [mDOWN],
            '-': [mLEFT, mRIGHT],
            '\\': [mRIGHT],
            '/': [mLEFT],
            '|': [mDOWN],
        },
        LEFT: {
            '.': [mLEFT],
            '-': [mLEFT],
            '\\': [mUP],
            '/': [mDOWN],
            '|': [mUP, mDOWN],
        },
        UP: {
            '.': [mUP],
            '-': [mLEFT, mRIGHT],
            '\\': [mLEFT],
            '/': [mRIGHT],
            '|': [mUP],
        }
    } 

    h = {}
    points = [[0, 0, RIGHT]]

    while len(points):
        p = points.pop(0)

        y, x, dir = p

        if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]):
            continue

        k = key3(y, x, dir)

        if k in h:
            continue

        h[k] = 0

        on = grid[y][x]

        for nd in dir_map[dir][on]:
            yy = y + nd[0]
            xx = x + nd[1]
            
            new_dir = 0
            if nd == mUP:
                new_dir = UP
            if nd == mDOWN:
                new_dir = DOWN
            if nd == mRIGHT:
                new_dir = RIGHT
            if nd == mLEFT:
                new_dir = LEFT

            points.append([yy, xx, new_dir])

    hh = {}
    for k in h:
        i, j, d = k.split(' ')
        nk = key(i, j)
        hh[nk] = 0

    return len(hh) 

# 00:41:07   1701, really happy with this too
def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    grid = []

    for index in range(len(data)):
        line = data[index]
        grid.append([c for c in line])
            

    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3

    mRIGHT = [0, 1]
    mDOWN = [1, 0]
    mLEFT = [0, -1]
    mUP = [-1, 0]

    dir_map = {
        RIGHT: {
            '.': [mRIGHT],
            '-': [mRIGHT],
            '\\': [mDOWN],
            '/': [mUP],
            '|': [mUP, mDOWN],
        },
        DOWN: {
            '.': [mDOWN],
            '-': [mLEFT, mRIGHT],
            '\\': [mRIGHT],
            '/': [mLEFT],
            '|': [mDOWN],
        },
        LEFT: {
            '.': [mLEFT],
            '-': [mLEFT],
            '\\': [mUP],
            '/': [mDOWN],
            '|': [mUP, mDOWN],
        },
        UP: {
            '.': [mUP],
            '-': [mLEFT, mRIGHT],
            '\\': [mLEFT],
            '/': [mRIGHT],
            '|': [mUP],
        }
    } 

    m = 0

    start = []

    # overlap, but oh well
    for i in range(len(grid)):
        start.append([i, 0, RIGHT])
        start.append([i, len(grid[i]) - 1, LEFT])

    for j in range(len(grid[0])):
        start.append([0, j, DOWN])
        start.append([len(grid) - 1, j, UP])

    for ss in start:
        h = {}
        points = [ss]

        while len(points):
            p = points.pop(0)

            y, x, dir = p

            if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]):
                continue

            k = key3(y, x, dir)

            if k in h:
                continue

            h[k] = 0

            on = grid[y][x]

            for nd in dir_map[dir][on]:
                yy = y + nd[0]
                xx = x + nd[1]
                
                new_dir = 0
                if nd == mUP:
                    new_dir = UP
                if nd == mDOWN:
                    new_dir = DOWN
                if nd == mRIGHT:
                    new_dir = RIGHT
                if nd == mLEFT:
                    new_dir = LEFT

                points.append([yy, xx, new_dir])

        hh = {}
        for k in h:
            i, j, d = k.split(' ')
            nk = key(i, j)
            hh[nk] = 0
        m = max(m, len(hh))

    return m 

print(f'part1: {part1()}')
print(f'part2: {part2()}')
