import sys
sys.path.insert(0, '../../')
import os
import math
from helper.helper import getFile

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()
    data = data.split('\n')

    h = {}
    hs = [{}, {}]

    for i in range(len(data)):
        x = 0
        y = 0
        line = data[i]
        moves = line.split(',')
        for move in moves:
            dir = move[0]
            num = int(move[1:])
        
            dx = 0
            dy = 0
            if dir == 'U':
                dy = -1
            if dir == 'D':
                dy = 1
            if dir == 'L':
                dx = -1
            if dir == 'R':
                dx = 1

            for k in range(num):
                x += dx
                y += dy
                key = f'{x} {y}'

                if key in hs[i]:
                    hs[i][key] += 1
                else:
                    hs[i][key] = 1

                if key in h:
                    h[key] += 1
                else:
                    h[key] = 1
    a = []

    for k in h:
        if h[k] > 1 and k in hs[0] and k in hs[1]:
            x, y = k.split(' ')
            x = int(x)
            y = int(y)
            a.append(abs(x) + abs(y))

    a.sort()

    return a[0] 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()
    data = data.split('\n')

    h = {}
    hs = [{}, {}]
    ds = [{}, {}]

    for i in range(len(data)):
        x = 0
        y = 0
        line = data[i]
        moves = line.split(',')
        d = 0
        for move in moves:
            dir = move[0]
            num = int(move[1:])
        
            dx = 0
            dy = 0
            if dir == 'U':
                dy = -1
            if dir == 'D':
                dy = 1
            if dir == 'L':
                dx = -1
            if dir == 'R':
                dx = 1

            for k in range(num):
                x += dx
                y += dy
                d += 1
                key = f'{x} {y}'

                if key in hs[i]:
                    hs[i][key] += 1
                else:
                    hs[i][key] = 1
                ds[i][key] = d

                if key in h:
                    h[key] += 1
                else:
                    h[key] = 1
    a = []

    for k in h:
        if h[k] > 1 and k in hs[0] and k in hs[1]:
            a.append(abs(ds[0][k]) + abs(ds[1][k]))

    a.sort()

    return a[0] 

print(f'part1: {part1()}')
print(f'part2: {part2()}')
