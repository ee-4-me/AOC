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

    for i in range(len(contents)):
        for j in range(i + 1, len(contents)):
            a = int(contents[i])
            b = int(contents[j])
            if a + b == 2020:
                return a * b

def part2():
    contents = getFile(os.path.join(os.curdir, 'input.txt'))
    # neovim being dumb 
    if contents.endswith('\n'):
        contents = contents[:-1]
    contents = contents.split('\n')

    for i in range(len(contents)):
        for j in range(i + 1, len(contents)):
            for k in range(j + 1, len(contents)):
                a = int(contents[i])
                b = int(contents[j])
                c = int(contents[k])
                if a + b + c== 2020:
                    return a * b * c

print(f'part1: {part1()}')
print(f'part2: {part2()}')
