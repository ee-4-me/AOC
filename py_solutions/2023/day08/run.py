import sys
sys.path.insert(0, '../../')
import os
import math
import copy
from helper.helper import getFile, mymap, myfilter, download_input, hash_string, hashes_equal

download_input(os.path.abspath(os.curdir))

# dog water time, did next day, super sloppy, used LCM tool online


# didn't read first part, started on line 1, not from 'AAA', thanks reddit
def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    sum = 0

    h = {}

    lrseq = data[0]
    for index in range(len(data)):
        line = data[index]
        s = line.split(' ')[0]
        if index <= 1:
            continue
        l = line.split('(')[1].split(',')[0]
        r = line.split(', ')[1].split(')')[0]
        h[s] = [l, r]
        
    i = 0
    pos = 'AAA'
    while True:
        dir = lrseq[i]
        i += 1
        if i == len(lrseq):
            i = 0

        off = 1
        if dir == 'L':
            off = 0

        pos = h[pos][off]
        sum += 1
        if pos == 'ZZZ':
            return sum

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    sum = 0

    h = {}

    startpos = []
    lrseq = data[0]
    for index in range(len(data)):
        line = data[index]
        s = line.split(' ')[0]
        if index <= 1:
            continue
        l = line.split('(')[1].split(',')[0]
        r = line.split(', ')[1].split(')')[0]
        if s[-1] == 'A':
            startpos.append(s)
        h[s] = [l, r]

    cycle = {} 

    i = 0
    sum = 0
    while True:
        dir = lrseq[i]
        i += 1
        if i == len(lrseq):
            i = 0

        off = 1
        if dir == 'L':
            off = 0

        sum += 1
        for j in range(len(startpos)):
            startpos[j] = h[startpos[j]][off]
            if startpos[j].endswith('Z'):
                if startpos[j] not in cycle:
                    cycle[startpos[j]] = sum
            
        cc = 0
        for k in cycle:
            cc += 1
        if cc == len(startpos):
            s = ''
            for k in cycle:
                s += str(cycle[k]) + ', '
            print(s)
            return 0

print(f'part1: {part1()}')
print(f'part2: {part2()}')
