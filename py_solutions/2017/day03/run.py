
import sys
sys.path.insert(0, '../../')
import os
import math
from helper.helper import getFile

def part1():
    target = 368078

    x = 0
    y = 0

    c = 0
    acc = 0.5
    dir = 1

    for i in range(1, target):
        dx = 0
        dy = 0

        if dir == 0:
            dy = -1
        if dir == 1:
            dx = 1
        if dir == 2:
            dy = 1
        if dir == 3:
            dx = -1

        x += dx
        y += dy
        
        c += 1
        if c >= acc:
            acc += 0.5
            c = 0
            dir += 1
            if dir == 4:
                dir = 0
    return abs(x) + abs(y)

def part2():
    target = 368078

    x = 0
    y = 0

    c = 0
    acc = 0.5
    dir = 1

    h = {}
    h['0 0'] = 1

    for i in range(1, target):
        dx = 0
        dy = 0

        if dir == 0:
            dy = -1
        if dir == 1:
            dx = 1
        if dir == 2:
            dy = 1
        if dir == 3:
            dx = -1

        x += dx
        y += dy

        a = 0
        if f'{x + 1} {y + 1}' in h:
            a += h[f'{x + 1} {y + 1}']
        if f'{x + 1} {y + 0}' in h:
            a += h[f'{x + 1} {y + 0}']
        if f'{x + 1} {y - 1}' in h:
            a += h[f'{x + 1} {y - 1}']

        if f'{x + 0} {y + 1}' in h:
            a += h[f'{x + 0} {y + 1}']
        if f'{x + 0} {y - 1}' in h:
            a += h[f'{x + 0} {y - 1}']

        if f'{x - 1} {y + 1}' in h:
            a += h[f'{x - 1} {y + 1}']
        if f'{x - 1} {y + 0}' in h:
            a += h[f'{x - 1} {y + 0}']
        if f'{x - 1} {y - 1}' in h:
            a += h[f'{x - 1} {y - 1}']

        if a > target:
            return a
        h[f'{x} {y}'] = a
        
        c += 1
        if c >= acc:
            acc += 0.5
            c = 0
            dir += 1
            if dir == 4:
                dir = 0

print(f'part1: {part1()}')
print(f'part2: {part2()}')

