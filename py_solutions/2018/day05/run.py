import sys
sys.path.insert(0, '../../')
import os
import math
import copy
from helper.helper import getFile, mymap, myfilter, download_input, hash_string, hashes_equal

download_input(os.path.abspath(os.curdir))

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')
    line = data[0]

    letters =    'abcdefghijklmnopqrstuvwxyz'
    capletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while True:
        l = len(line)
        for i in range(len(letters)):
            s1 = letters[i] + capletters[i]
            s2 = capletters[i] + letters[i]
            line = line.replace(s1, '')
            line = line.replace(s2, '')
        if len(line) == l:
            return l

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')
    line1 = data[0]

    letters =    'abcdefghijklmnopqrstuvwxyz'
    capletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    ans = []
    for j in range(len(letters)):
        line = copy.deepcopy(line1)
        line = line.replace(letters[j], '')
        line = line.replace(capletters[j], '')

        while True:
            l = len(line)
            for i in range(len(letters)):
                s1 = letters[i] + capletters[i]
                s2 = capletters[i] + letters[i]
                line = line.replace(s1, '')
                line = line.replace(s2, '')
            if len(line) == l:
                ans.append(l)
                break
    return min(ans)

print(f'part1: {part1()}')
print(f'part2: {part2()}')
