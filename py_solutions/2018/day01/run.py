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

    sum = 0

    for line in contents:
        sum += int(line)

    return sum

def part2():
    contents = getFile(os.path.join(os.curdir, 'input.txt'))
    # neovim being dumb 
    if contents.endswith('\n'):
        contents = contents[:-1]
    contents = contents.split('\n')

    sum = 0
    h = {}
    h[0] = 0

    while True:
        for line in contents:
            sum += int(line)
            if sum in h:
                return sum
            h[sum] = 0

print(f'part1: {part1()}')
print(f'part2: {part2()}')
