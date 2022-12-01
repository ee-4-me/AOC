import sys
sys.path.insert(0, '../../')
import os
import math
from helper.helper import getFile

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt'))
    while data.endswith('\n'):
        data = data[:-1]

    data = data.split('\n')
    print(data)

    sum = 0

    for i in range(len(data)):
        line = data[i]
        print(line)
        
    return sum 

def part2():
    pass

print(f'part1: {part1()}')
print(f'part2: {part2()}')
