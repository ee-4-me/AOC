import sys
sys.path.insert(0, '../../')
import os
import math
import copy
from helper.helper import getFile, mymap, myfilter, download_input, hash_string, hashes_equal

download_input(os.path.abspath(os.curdir), '53616c7465645f5f62fa34767db5d49196e9adc99b8b76629de3b8bb0641f3e8227bbb21f99481462cbbf0046b42eb539f2b7388114025ca4c4fa394014337f9')

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()
    data = data.split('\n')[0]
    start, end = mymap(data.split('-'), lambda x: int(x))

    sum = 0

    for i in range(start, end):
        n = str(i)

        flag = True
        pair = False
        for j in range(1, len(n)):
            if n[j] < n[j - 1]:
                flag = False
            if n[j] == n[j - 1]:
                pair = True
        if pair and flag:
            sum += 1

    return sum 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()
    data = data.split('\n')[0]
    start, end = mymap(data.split('-'), lambda x: int(x))

    sum = 0

    for i in range(start, end):
        n = str(i)

        flag = True
        h = {}

        for j in range(len(n)):
            if j >= 1:
                if n[j] < n[j - 1]:
                    flag = False

            c = n[j]
            if c not in h:
                h[c] = 1
            else:
                h[c] += 1

        twoc = False
        for k in h:
            if h[k] == 2:
                twoc = True

        if flag and twoc:
            sum += 1

    return sum 

print(f'part1: {part1()}')
print(f'part2: {part2()}')
