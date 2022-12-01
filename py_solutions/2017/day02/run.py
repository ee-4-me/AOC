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
        row = (line.split('\t'))
        a = []
        for cell in row:
            cell = int(cell)
            a.append(cell)
        a.sort(reverse=True)
        sum += a[0] - a[-1]

    return sum 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt'))
    while data.endswith('\n'):
        data = data[:-1]

    data = data.split('\n')

    sum = 0

    for k in range(len(data)):
        line = data[k]
        row = (line.split('\t'))
        flag = False
        for i in range(len(row)):
            if flag:
                break
            for j in range(i + 1, len(row)):
                cell1 = int(row[i])
                cell2 = int(row[j])
                if max(cell1, cell2) % min(cell1, cell2) == 0:
                    sum += max(cell1, cell2) / min(cell1, cell2)
                    flag = True
                    break

    return sum 

print(f'part1: {part1()}')
print(f'part2: {part2()}')
