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

    contents += contents[0]

    for i in range(1, len(contents)):
        if contents[i - 1] == contents[i]:
            sum += int(contents[i])

    return sum

def part2():
    contents = getFile(os.path.join(os.curdir, 'input.txt'))
    # neovim being dumb 
    if contents.endswith('\n'):
        contents = contents[:-1]
    contents = contents.split('\n')
    contents = contents[0]

    sum = 0
    l = len(contents)
    contents += contents

    for i in range(l):
        if contents[i] == contents[i + l // 2]:
            sum += int(contents[i])

    return sum

print(f'part1: {part1()}')
print(f'part2: {part2()}')
