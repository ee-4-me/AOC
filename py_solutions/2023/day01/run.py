import sys
sys.path.insert(0, '../../')
import os
import math
from helper.helper import getFile
from copy import deepcopy

# 3:28 / 992 - took a second to enter number lol

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt'))
    while data.endswith('\n'):
        data = data[:-1]

    data = data.split('\n')

    sum = 0

    for i in range(len(data)):
        line = data[i]
        a = 0
        for c in line:
            if c.isdigit():
                a += 10 * int(c)
                break
        for c in line[::-1]:
            if c.isdigit():
                a += int(c)
                break
        sum += a
    return sum 


# 25:37 / 2602 - oof, didn't read problem fully, thought only allowed were spelled digits (not both)
# made some silly mistakes with deepcopy, and had some slopy code ngl lol

h = ['!', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt'))
    while data.endswith('\n'):
        data = data[:-1]

    data = data.split('\n')

    sum = 0

    for j in range(len(data)):
        line = data[j]
        line1 = deepcopy(line)
        line2 = deepcopy(line)
        while len(line1):
            if line1[0].isdigit():
                sum += 10 * int(line1[0])
                break
            for i in range(len(h)):
                if line1.startswith(h[i]):
                    sum += 10 * i
                    line1 = ''
                    break
            line1 = line1[1:]
        while len(line2):
            if line2[-1].isdigit():
                sum += int(line2[-1])
                break
            for i in range(len(h)):
                if line2.endswith(h[i]):
                    sum += i
                    line2 = ''
                    break
            line2 = line2[:-1]
    return sum 


print(f'part1: {part1()}')
print(f'part2: {part2()}')
