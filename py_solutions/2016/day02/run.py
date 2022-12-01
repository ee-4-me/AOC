import sys
sys.path.insert(0, '../../')
import os
import math
from helper.helper import getFile

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt'))
    while data.endswith('\n'):
        data = data[:-1]

    data = data.split('\n')

    keypad = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
    ] 
    x = 1
    y = 1

    ans = ''

    for i in range(len(data)):
        line = data[i]

        for c in line:
            if c == 'R':
                x += 1
                if x > 2:
                    x = 2
            if c == 'L':
                x -= 1
                if x < 0:
                    x = 0
            if c == 'U':
                y -= 1
                if y < 0:
                    y = 0
            if c == 'D':
                y += 1
                if y > 2:
                    y = 2

        ans = ans + keypad[y][x] 

    return ans 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt'))
    while data.endswith('\n'):
        data = data[:-1]

    data = data.split('\n')

    keypad = {}
    keypad['-2 0'] = '1'
    keypad['-1 -1'] = '2'
    keypad['-1 0'] = '3'
    keypad['-1 1'] = '4'
    keypad['0 -2'] = '5'
    keypad['0 -1'] = '6'
    keypad['0 0'] = '7'
    keypad['0 1'] = '8'
    keypad['0 2'] = '9'
    keypad['1 -1'] = 'A'
    keypad['1 0'] = 'B'
    keypad['1 1'] = 'C'
    keypad['2 0'] = 'D'
    x = 0
    y = 0

    ans = ''

    for i in range(len(data)):
        line = data[i]

        for c in line:
            if c == 'R':
                x += 1
                if f'{y} {x}' not in keypad:
                    x -= 1
            if c == 'L':
                x -= 1
                if f'{y} {x}' not in keypad:
                    x += 1
            if c == 'U':
                y -= 1
                if f'{y} {x}' not in keypad:
                    y += 1
            if c == 'D':
                y += 1
                if f'{y} {x}' not in keypad:
                    y -= 1

        ans = ans + keypad[f'{y} {x}']

    return ans 

print(f'part1: {part1()}')
print(f'part2: {part2()}')
