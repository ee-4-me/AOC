import sys
sys.path.insert(0, '../../')
import os
import math
from helper.helper import getFile, mymap, myfilter, download_input, hash_string, hashes_equal

download_input(os.path.abspath(os.curdir))

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()
    data = data.split('\n')

    sum = 0

    for index in range(len(data)):
        h = {}
        line = data[index]
        flag = True
        for word in line.split(' '):
            if word in h:
                flag = False
                break
            h[word] = 0
        if flag:
            sum += 1

        
    return sum 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()
    data = data.split('\n')

    sum = 0

    for index in range(len(data)):
        line = data[index]
        hs = []

        words = line.split(' ')
        for word in words:
            hs.append(hash_string(word))

        no_same = True
        for i in range(len(hs)):
            if not no_same:
                break
            for j in range(i + 1, len(hs)):
                if hashes_equal(hs[i], hs[j]):
                    no_same = False
                    break

        if no_same:
            sum += 1

    return sum 

print(f'part1: {part1()}')
print(f'part2: {part2()}')
