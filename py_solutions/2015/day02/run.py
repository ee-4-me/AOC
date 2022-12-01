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

    sum = 0

    for i in range(len(data)):
        line = data[i]
        l, w, h = line.split('x')
        l, w, h = int(l), int(w), int(h)

        a = l * w
        b = l * h
        c = h * w
        e = min(a, b, c)
        sum += 2 * (a + b + c) + e
        
    return sum 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt'))
    while data.endswith('\n'):
        data = data[:-1]

    data = data.split('\n')

    sum = 0

    for i in range(len(data)):
        line = data[i]
        l, w, h = line.split('x')
        l, w, h = int(l), int(w), int(h)

        m = max(l, w, h)
        e = 2 * (l + w + h - m)
        v = l * w * h 
        sum += e + v
    return sum 

print(f'part1: {part1()}')
print(f'part2: {part2()}')
