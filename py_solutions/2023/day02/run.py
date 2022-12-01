import sys
sys.path.insert(0, '../../')
import os
import math
from helper.helper import getFile, mymap, myfilter, download_input

download_input(os.path.abspath(os.curdir), '')

# 1069 - 09:19, pretty happy

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    sum = 0
    r = 12
    g = 13
    b = 14

    for index in range(len(data)):
        line = data[index]
        l = line.split(' ')
        id = int(l[1][:-1])
        line = line.split(': ')[1]
        rounds = line.split('; ')
        flag = True
        for round in rounds:
            matches = round.split(', ')
            for match in matches:
               n, color = match.split(' ')
               n = int(n)
               if color[0] == 'r'and n > r:
                   flag = False
               if color[0] == 'g'and n > g:
                   flag = False
               if color[0] == 'b'and n > b:
                   flag = False
        if flag:
            sum += id

    return sum 

# 4998 - 29:08, input parsing

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    sum = 0

    for index in range(len(data)):
        line = data[index]
        line = line.split(': ')[1]
        rounds = line.split('; ')
        rm = 0
        gm = 0
        bm = 0
        for round in rounds:
            matches = round.split(', ')
            for match in matches:
               n, color = match.split(' ')
               n = int(n)
               if color[0] == 'r':
                   rm = max(rm, n)
               if color[0] == 'g':
                   gm = max(gm, n)
               if color[0] == 'b':
                   bm = max(bm, n)

        sum += rm * gm * bm 

    return sum 

print(f'part1: {part1()}')
print(f'part2: {part2()}')
