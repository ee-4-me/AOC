import sys
from typing import cast
sys.path.insert(0, '../../')
import os
import math
from helper.helper import getFile
from copy import deepcopy

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')[0].split(',')
    data = list(map(lambda x: int(x), data))
    
    i = 0
    while data[i] != 99:
        if data[i] == 1:
            data[data[i + 3]] = data[data[i + 1]] + data[data[i + 2]]
        if data[i] == 2:
            data[data[i + 3]] = data[data[i + 1]] * data[data[i + 2]]
        i += 4

    return data[0] 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')[0].split(',')
    data = list(map(lambda x: int(x), data))
    real_data = deepcopy(data)
    
    for j in range(100):
        for k in range(100):
            data = deepcopy(real_data)
            data[1] = j
            data[2] = k
            i = 0
            while data[i] != 99:
                if data[i] == 1:
                    data[data[i + 3]] = data[data[i + 1]] + data[data[i + 2]]
                if data[i] == 2:
                    data[data[i + 3]] = data[data[i + 1]] * data[data[i + 2]]
                i += 4
            if data[0] == 19690720:
                return 100 * j + k

print(f'part1: {part1()}')
print(f'part2: {part2()}')
