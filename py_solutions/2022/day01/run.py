import sys
sys.path.insert(0, '../../')
import os
import math
from helper.helper import getFile

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt'))
    while data.endswith('\n'):
        data = data[:-1]
    data = data.split('\n\n')

    m = 0

    for i in range(len(data)):
        group = data[i].split('\n')
        sum = 0
        for j in range(len(group)):
            line = group[j]
            sum += int(line)
        m = max(m, sum)
        
    return m 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt'))
    while data.endswith('\n'):
        data = data[:-1]
    data = data.split('\n\n')

    a = []

    for i in range(len(data)):
        group = data[i].split('\n')
        sum = 0
        for j in range(len(group)):
            line = group[j]
            sum += int(line)
        a.append(sum)
        
    a.sort(reverse=True)

    return a[0] + a[1] + a[2] 

print(f'part1: {part1()}')
print(f'part2: {part2()}')
