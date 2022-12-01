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

    two = 0
    three = 0

    for i in range(len(data)):
        line = data[i]
        
        h = {}
        for c in line:
            if c in h:
                h[c] += 1
            else:
                h[c] = 1

        ltwo = 0
        lthree = 0
        for c in h:
            if int(h[c]) == 3:
                lthree = 1
            if int(h[c]) == 2:
                ltwo = 1

        two += ltwo
        three += lthree

    return two * three 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt'))
    while data.endswith('\n'):
        data = data[:-1]

    data = data.split('\n')

    for i in range(len(data)):
        line1 = data[i]
        for j in range(i + 1, len(data)):
            line2 = data[j]
        
            misses = 0
            for k in range(len(line1)):
                if line1[k] != line2[k]:
                    misses += 1
            if misses == 1:
                a = ''
                for k in range(len(line1)):
                    if line1[k] == line2[k]:
                        a += line1[k]
                return a

print(f'part1: {part1()}')
print(f'part2: {part2()}')
