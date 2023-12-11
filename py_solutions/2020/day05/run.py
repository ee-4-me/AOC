import sys
sys.path.insert(0, '../../')
import os
import math
import copy
from helper.helper import getFile, mymap, myfilter, download_input, hash_string, hashes_equal

download_input(os.path.abspath(os.curdir))

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    a = []

    for index in range(len(data)):
        line = data[index]
        fb = line[:7]
        rl = line[7:]
        fb = int(fb.replace('F', '0').replace('B', '1'), 2)
        rl = int(rl.replace('L', '0').replace('R', '1'), 2)
        a.append(fb * 8 + rl)

    return max(a) 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    a = []

    for index in range(len(data)):
        line = data[index]
        fb = line[:7]
        rl = line[7:]
        fb = int(fb.replace('F', '0').replace('B', '1'), 2)
        rl = int(rl.replace('L', '0').replace('R', '1'), 2)
        a.append(fb * 8 + rl)

    a.sort()
    for i in range(1, len(a)):
        if a[i] - a[i - 1] != 1:
          return a[i] - 1

print(f'part1: {part1()}')
print(f'part2: {part2()}')
