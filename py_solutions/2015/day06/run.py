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

    n_lights = 1000

    grid = {}

    for i in range(n_lights):
        for j in range(n_lights):
            grid[(i, j)] = 0

    for index in range(len(data)):
        line = data[index]


        line = line.split(' ')
        action = ''

        for word in ['on', 'off', 'toggle']:
            if word in line:
                action = word
                break

        start = line[-3]
        end = line[-1]

        start_x, start_y = [int(x) for x in start.split(',')]
        end_x, end_y = [int(x) for x in end.split(',')]


        for i in range(min(start_y, end_y), max(start_y, end_y) + 1):
            for j in range(min(start_x, end_x), max(start_x, end_x) + 1):

                pos = (i, j)
                if action == 'on':
                    grid[pos] = 1
                elif action == 'off':
                    grid[pos] = 0
                else:
                    grid[pos] ^= 1

    ans = 0

    for k in grid:
        if grid[k] == 1:
            ans += 1
        
    return ans 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    n_lights = 1000

    grid = {}

    for i in range(n_lights):
        for j in range(n_lights):
            grid[(i, j)] = 0

    for index in range(len(data)):
        line = data[index]


        line = line.split(' ')
        action = ''

        for word in ['on', 'off', 'toggle']:
            if word in line:
                action = word
                break

        start = line[-3]
        end = line[-1]

        start_x, start_y = [int(x) for x in start.split(',')]
        end_x, end_y = [int(x) for x in end.split(',')]


        for i in range(min(start_y, end_y), max(start_y, end_y) + 1):
            for j in range(min(start_x, end_x), max(start_x, end_x) + 1):

                pos = (i, j)
                if action == 'on':
                    grid[pos] += 1
                elif action == 'off':
                    grid[pos] -= 1
                    if grid[pos] < 0:
                        grid[pos] = 0
                else:
                    grid[pos] += 2

    ans = 0

    for k in grid:
        ans += grid[k]
        
    return ans 

print(f'part1: {part1()}')
print(f'part2: {part2()}')
