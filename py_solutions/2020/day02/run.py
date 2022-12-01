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
        nums, letter, string = line.split(' ')
        minn = int(nums.split('-')[0])
        maxn = int(nums.split('-')[1])
        letter = letter[0]

        a = 0
        for c in string:
            if c == letter:
                a += 1
        if a >= minn and a <= maxn:
            sum += 1

    return sum 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    sum = 0

    for i in range(len(data)):
        line = data[i]
        nums, letter, string = line.split(' ')
        minn = int(nums.split('-')[0])
        maxn = int(nums.split('-')[1])
        letter = letter[0]

        a = 0
        if string[maxn - 1] == letter:
            a += 1
        if string[minn - 1] == letter:
            a += 1
        if a == 1:
            sum += 1

    return sum 

print(f'part1: {part1()}')
print(f'part2: {part2()}')
