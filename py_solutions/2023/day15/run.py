import sys
sys.path.insert(0, '../../')
import os
import math
import copy
from itertools import permutations
from helper.helper import getFile, mymap, myfilter, download_input, hash_string, hashes_equal, key

download_input(os.path.abspath(os.curdir))

def hash(s):
    sum = 0
    for c in s:
        n = ord(c)
        sum += n
        sum *= 17
        sum = sum % 256
    return sum

# started late, maybe could have been competetive?
# 00:35:47   6898

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')[0].split(',')

    sum = 0

    for index in range(len(data)):
        line = data[index]
        sum += hash(line)
    return sum 


# also could have been much faster if I started earlier
# 00:58:48   4944
def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')[0].split(',')

    sum = 0

    h = {}
    for index in range(len(data)):
        line = data[index]
        label = ''
        dash = '-' in line
        n = 0

        if dash:
            label = line.split('-')[0]
        else:
            label, n = line.split('=')
            n = int(n)

        hashn = hash(label)

        if hashn not in h:
            h[hashn] = []

        if not dash:
            broke = False
            for i in range(len(h[hashn])):
                item = h[hashn][i]
                if item[0] == label:
                    h[hashn][i] = [label, n]
                    broke = True
                    break
            if not broke:
                h[hashn].append([label, n])
        else:
            for i in range(len(h[hashn])):
                item = h[hashn][i]
                if item[0] == label:
                    del h[hashn][i]
                    break

    for k in h:
        for i in range(len(h[k])):
            item = h[k][i]
            sum += (int(k) + 1) * (i + 1) * item[1]

    return sum 

print(f'part1: {part1()}')
print(f'part2: {part2()}')
