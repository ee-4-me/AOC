import sys
sys.path.insert(0, '../../')
import os
import math
from helper.helper import getFile, mymap, myfilter, download_input

download_input(os.path.abspath(os.curdir))

# 1009 - 5:45, pretty happy

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')
    sum = 0

    for index in range(len(data)):
        line = data[index]
        
        win, have = line.split(': ')[1].split(' | ') 
        win = myfilter(win.split(' '), lambda x: x != '')
        win = [int(x) for x in win]
        have = myfilter(have.split(' '), lambda x: x != '')
        have = [int(x) for x in have]

        a = 0
        for h in have:
            if h in win:
                if a == 0:
                    a = 1
                else:
                    a *= 2
        sum += a 
    return sum 

# 5067 - 33:26, didn't understand what I was supposed to do for a long time

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()
    data = data.split('\n')
    sum = 0

    ha = {}

    for i in range(len(data)):
        ha[i] = 1

    for index in range(len(data)):
        line = data[index]
        
        win, have = line.split(': ')[1].split(' | ') 
        win = myfilter(win.split(' '), lambda x: x != '')
        win = [int(x) for x in win]
        have = myfilter(have.split(' '), lambda x: x != '')
        have = [int(x) for x in have]

        a = []
        for h in have:
            if h in win:
                a.append(h)

        c = ha[index]

        for i in range(len(a)):
            k = index + 1 + i
            
            if k in ha:
                ha[k] += c
            else:
                ha[k] = c

    sum = 0
    for k in ha:
        sum += ha[k]

    return sum 

print(f'part1: {part1()}')
print(f'part2: {part2()}')
