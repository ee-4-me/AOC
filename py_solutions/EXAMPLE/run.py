import sys
sys.path.insert(0, '../../')
import os
import math
import copy
from itertools import permutations
from helper.helper import getFile, mymap, myfilter, download_input, hash_string, hashes_equal, key

download_input(os.path.abspath(os.curdir))

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')
    print(data)

    sum = 0

    for index in range(len(data)):
        line = data[index]
        print(line)
        
    return sum 

def part2():
    pass

print(f'part1: {part1()}')
print(f'part2: {part2()}')
