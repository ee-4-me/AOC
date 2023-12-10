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

    sum = 0

    for index in range(len(data)):
        line = data[index]
        h = hash_string(line)

        flag = True

        vc = 0
        for c in 'aeiou':
            if c in h:
                vc += h[c] 

        if vc < 3:
            flag = False

        dup = False
        for i in range(1, len(line)):
            if line[i] == line[i - 1]:
                dup = True

        if not dup:
            flag = False

        for ss in ['ab', 'cd', 'pq', 'xy']:
            if ss in line:
                flag = False

        if flag:
            sum += 1

    return sum 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    sum = 0

    for index in range(len(data)):
        line = data[index]
        h = hash_string(line)

        flag = True


        h2 = {}
        for i in range(1, len(line)):
            k = line[i - 1] + line[i]
            if k not in h2:
                h2[k] = [i]
            else:
                h2[k].append(i)
        found = False

        for k in h2:
            if len(h2[k]) > 2:
                found = True
            if len(h2[k]) == 2:
                if abs(h2[k][0] - h2[k][1]) > 1:
                    found = True
        if not found:
            flag = False

        dup = False
        for i in range(2, len(line)):
            if line[i] == line[i - 2]:
                dup = True

        if not dup:
            flag = False

        if flag:
            sum += 1

    return sum 

print(f'part1: {part1()}')
print(f'part2: {part2()}')
