import sys
sys.path.insert(0, '../../')
import os
import math
from helper.helper import getFile

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    h = {}

    for index in range(len(data)):
        line = data[index]
        line = line.split(' ')
        x,y = line[2][:-1].split(',')
        x = int(x)
        y = int(y)

        w,l = line[3].split('x')
        w = int(w)
        l = int(l)

        for j in range(x, x + w):
            for i in range(y, y + l):
                key = f'{j} {i}'
                if key in h:
                    h[key] += 1
                else:
                    h[key] = 1
        
    sum = 0
    for k in h:
        if h[k] > 1:
            sum += 1

    return sum 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    h = {}

    for index in range(len(data)):
        line = data[index]
        line = line.split(' ')
        x,y = line[2][:-1].split(',')
        x = int(x)
        y = int(y)

        w,l = line[3].split('x')
        w = int(w)
        l = int(l)

        for j in range(x, x + w):
            for i in range(y, y + l):
                key = f'{j} {i}'
                if key in h:
                    h[key] += 1
                else:
                    h[key] = 1

    for index in range(len(data)):
        line = data[index]
        line = line.split(' ')
        id = line[0][1:]
        x,y = line[2][:-1].split(',')
        x = int(x)
        y = int(y)

        w,l = line[3].split('x')
        w = int(w)
        l = int(l)

        match = 0
        for j in range(x, x + w):
            for i in range(y, y + l):
                key = f'{j} {i}'
                if h[key] > 1:
                    match += 1
        if match == 0:
            return id

print(f'part1: {part1()}')
print(f'part2: {part2()}')
