import sys
sys.path.insert(0, '../../')
import os
import math
from helper.helper import getFile, mymap, myfilter

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')
    print(data)

    sum = 0

    j = 0

    for index in range(len(data)):
        line = data[index]
        if line[j] == '#':
            sum += 1
        j += 3
        if j >= len(line):
            j -= len(line)
        
    return sum 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    sum = 1

    for dx, dy in [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2],
    ]:
        j = 0

        ans = 0
        for index in range(0, len(data), dy):
            line = data[index]
            if line[j] == '#':
                ans += 1
            j += dx
            if j >= len(line):
                j -= len(line)
            
        sum *= ans

    return sum

print(f'part1: {part1()}')
print(f'part2: {part2()}')
