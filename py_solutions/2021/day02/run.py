import sys
sys.path.insert(0, '../../')
import os
import math
from helper.helper import getFile

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    x = 0
    y = 0

    for i in range(len(data)):
        line = data[i]
        dir, amount = line.split(' ')
        amount = int(amount)

        if dir == 'up':
            y -= amount
        if dir == 'down':
            y += amount
        if dir == 'forward':
            x += amount
        
    return y * x

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    x = 0
    y = 0
    aim = 0

    for i in range(len(data)):
        line = data[i]
        dir, amount = line.split(' ')
        amount = int(amount)

        if dir == 'up':
            aim -= amount
        if dir == 'down':
            aim += amount
        if dir == 'forward':
            x += amount
            y += aim * amount    
        
    return y * x

print(f'part1: {part1()}')
print(f'part2: {part2()}')
