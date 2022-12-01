import sys
sys.path.insert(0, '../../')
import os
import math
from helper.helper import getFile

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    sum = 0

    for i in range(len(data)):
        line = data[i]
        a, b = line.split(' ')

        if b == 'X':
            sum += 1
        if b == 'Y':
            sum += 2
        if b == 'Z':
            sum += 3

        if a == 'A' and b == 'X':
            sum += 3
        if a == 'B' and b == 'Y':
            sum += 3
        if a == 'C' and b == 'Z':
            sum += 3

        if a == 'A' and b == 'Y':
            sum += 6
        if a == 'A' and b == 'Z':
            sum += 0
        if a == 'B' and b == 'X':
            sum += 0
        if a == 'B' and b == 'Z':
            sum += 6
        if a == 'C' and b == 'X':
            sum += 6
        if a == 'C' and b == 'Y':
            sum += 0
        
    return sum 

# why think when I can code?
def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    sum = 0

    for i in range(len(data)):
        line = data[i]
        a, b = line.split(' ')

        if b == 'X' and a == 'A':
            b = 'Z'
        elif b == 'Y' and a == 'A':
            b = 'X'
        elif b == 'Z' and a == 'A':
            b = 'Y'
        elif b == 'X' and a == 'B':
            b = 'X'
        elif b == 'Y' and a == 'B':
            b = 'Y'
        elif b == 'Z' and a == 'B':
            b = 'Z'
        elif b == 'X' and a == 'C':
            b = 'Y'
        elif b == 'Y' and a == 'C':
            b = 'Z'
        elif b == 'Z' and a == 'C':
            b = 'X'

        if b == 'X':
            sum += 1
        if b == 'Y':
            sum += 2
        if b == 'Z':
            sum += 3

        if a == 'A' and b == 'X':
            sum += 3
        if a == 'B' and b == 'Y':
            sum += 3
        if a == 'C' and b == 'Z':
            sum += 3

        if a == 'A' and b == 'Y':
            sum += 6
        if a == 'A' and b == 'Z':
            sum += 0
        if a == 'B' and b == 'X':
            sum += 0
        if a == 'B' and b == 'Z':
            sum += 6
        if a == 'C' and b == 'X':
            sum += 6
        if a == 'C' and b == 'Y':
            sum += 0
        
    return sum 

print(f'part1: {part1()}')
print(f'part2: {part2()}')
