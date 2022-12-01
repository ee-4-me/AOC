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
        sum += max(int(line) // 3 - 2, 0)

    return sum

def part2():
    contents = getFile(os.path.join(os.curdir, 'input.txt'))
    # neovim being dumb 
    if contents.endswith('\n'):
        contents = contents[:-1]
    contents = contents.split('\n')

    sum = 0

    for line in contents:
        x = max(int(line) // 3 - 2, 0)
        sum += x
        while x > 0:
            x = max(x // 3 - 2, 0)
            sum += x
        
    return sum

print(f'part1: {part1()}')
print(f'part2: {part2()}')
