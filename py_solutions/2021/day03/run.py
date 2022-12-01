import sys
sys.path.insert(0, '../../')
import os
import math
import copy
from helper.helper import getFile, mymap, myfilter, download_input

download_input(os.path.abspath(os.curdir), '')

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    l = len(data[0])
    a = ''
    b = ''
    for j in range(l):
        ones = 0
        for index in range(len(data)):
            line = data[index]
            if line[j] == '1':
                ones += 1
        if ones > len(data) / 2:
            a += '1'
            b += '0'
        else:
            a += '0'
            b += '1'

    return int(a, 2) * int(b, 2)

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')
    d1 = copy.deepcopy(data)
    d2 = copy.deepcopy(data)
    l = len(data[0])

    for j in range(l):
        ones = 0
        for index in range(len(d1)):
            line = d1[index]
            if line[j] == '1':
                ones += 1

        flag = '0'
        if ones >= len(d1) / 2:
            flag = '1'

        arr = []
        for index in range(len(d1)):
            line = d1[index]
            if line[j] == flag:
                arr.append(line)
        d1 = copy.deepcopy(arr)

    for j in range(l):
        if len(d2) == 1:
            break
        ones = 0
        for index in range(len(d2)):
            line = d2[index]
            if line[j] == '1':
                ones += 1

        flag = '0'
        if ones >= len(d2) / 2:
            flag = '1'

        arr = []
        for index in range(len(d2)):
            line = d2[index]
            if line[j] != flag:
                arr.append(line)
        d2 = copy.deepcopy(arr)

    return int(d1[0], 2) * int(d2[0], 2)

print(f'part1: {part1()}')
print(f'part2: {part2()}')
