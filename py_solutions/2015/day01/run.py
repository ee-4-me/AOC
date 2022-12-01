import sys
sys.path.insert(0, '../../')
from helper.helper import getFile
import os
import math

def part1():
    contents = getFile(os.path.join(os.curdir, 'input.txt'))
    # neovim being dumb 
    if contents.endswith('\n'):
        contents = contents[:-1]
    contents = contents.split('\n')
    contents = contents[0]

    sum = 0

    for i, item in enumerate(contents):
        if item == '(':
            sum = sum + 1

        if item == ')':
            sum = sum - 1

    return sum

def part2():
    contents = getFile(os.path.join(os.curdir, 'input.txt'))
    # neovim being dumb 
    if contents.endswith('\n'):
        contents = contents[:-1]
    contents = contents.split('\n')
    contents = contents[0]

    sum = 0

    for i, item in enumerate(contents):
        if item == '(':
            sum = sum + 1

        if item == ')':
            sum = sum - 1

        if sum < 0:
            return i + 1

    return 0

print(f'part1: {part1()}')
print(f'part2: {part2()}')
