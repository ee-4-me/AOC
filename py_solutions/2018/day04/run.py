import sys
sys.path.insert(0, '../../')
import os
import math
import copy
from helper.helper import getFile, mymap, myfilter, download_input, hash_string, hashes_equal

download_input(os.path.abspath(os.curdir), '53616c7465645f5f62fa34767db5d49196e9adc99b8b76629de3b8bb0641f3e8227bbb21f99481462cbbf0046b42eb539f2b7388114025ca4c4fa394014337f9')

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    data = sorted(data, key = lambda x: int(x.split('-')[1]) * 31 * 24 * 60 * 60 + int(x.split('-')[2].split(' ')[0]) * 24 * 60 * 60 + int(x.split(' ')[1].split(':')[0]) * 60 * 60 + int(x.split(':')[1].split(']')[0]))

    h = {}

    guard = 0
    start = 0
    end = 0
    for index in range(len(data)):
        line = data[index]
        if 'Guard' in line:
            guard = int(line.split('#')[1].split(' ')[0])
        if 'falls' in line:
            start = int(line.split(':')[1].split(']')[0])
        if 'wakes' in line:
            end = int(line.split(':')[1].split(']')[0])
            s = end - start

            if guard not in h:
                h[guard] = [[s, start, end]]
            else:
                h[guard].append([s, start, end])


    m = 0
    gn = 0

    for guard in h:
        s = 0
        for time in h[guard]:
            s += time[0]
        if s > m:
            m = s
            gn = guard

    th = {}
    for time in h[gn]:
        for i in range(time[1], time[2]):
            if i not in th:
                th[i] = 1
            else:
                th[i] += 1

    m = 0
    t = 0
    for k in th:
        if th[k] > m:
            m = th[k]
            t = k

    return t * gn

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    data = sorted(data, key = lambda x: int(x.split('-')[1]) * 31 * 24 * 60 * 60 + int(x.split('-')[2].split(' ')[0]) * 24 * 60 * 60 + int(x.split(' ')[1].split(':')[0]) * 60 * 60 + int(x.split(':')[1].split(']')[0]))

    hs = {} 

    guard = 0
    start = 0
    end = 0

    for index in range(len(data)):
        line = data[index]
        if 'Guard' in line:
            guard = int(line.split('#')[1].split(' ')[0])
        if 'falls' in line:
            start = int(line.split(':')[1].split(']')[0])
        if 'wakes' in line:
            end = int(line.split(':')[1].split(']')[0])
            for i in range(start, end):
                if i not in hs:
                    hs[i] = {}
                if guard not in hs[i]:
                    hs[i][guard] = 0
                hs[i][guard] += 1
            
    m = 0
    t = 0
    g = 0

    for time in hs:
        for guard in hs[time]:
            s = hs[time][guard]
            if s > m:
                m = s
                t = time
                g = guard

    return t * g

print(f'part1: {part1()}')
print(f'part2: {part2()}')
