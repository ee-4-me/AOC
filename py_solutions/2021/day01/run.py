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

    for i in range(1, len(contents)):
        if int(contents[i]) > int(contents[i - 1]):
            sum += 1

    return sum

def part2():
    contents = getFile(os.path.join(os.curdir, 'input.txt'))
    # neovim being dumb 
    if contents.endswith('\n'):
        contents = contents[:-1]
    contents = contents.split('\n')

    sum = 0

    for i in range(3, len(contents)):
        if int(contents[i]) > int(contents[i - 3]):
            sum += 1

    return sum

print(f'part1: {part1()}')
print(f'part2: {part2()}')
