import sys
sys.path.insert(0, '../../')
import os
import math
import copy
from helper.helper import getFile, mymap, myfilter, download_input, hash_string, hashes_equal

download_input(os.path.abspath(os.curdir))

# 10:53:43  48104
def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    d = []
    t = []
    for index in range(len(data)):
        line = data[index]
        line = myfilter(line.split(' '), lambda x: x != '')
        if line[0][0] == 'T':
            t = [int(x) for x in line[1:]]
        else:
            d = [int(x) for x in line[1:]]
        
    # ways you can win
    
    ans = []
    for i in range(len(d)):
        a = 0
        dist = d[i]
        time = t[i]

        for j in range(0, time):
            if j * (time - j) > dist:
                a += 1
        ans.append(a)

    sum = 1

    for a in ans:
        sum *= a

    return sum 

# 10:57:16  46655
def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    d = 0
    t = 0
    for index in range(len(data)):
        line = data[index]
        line = myfilter(line.split(' '), lambda x: x != '')
        if line[0][0] == 'T':
            t = int(''.join(line[1:]))
        else:
            d = int(''.join(line[1:]))
        
    # ways you can win
    
    a = 0

    for j in range(0, t):
        if j * (t - j) > d:
            a += 1

    return a 

print(f'part1: {part1()}')
print(f'part2: {part2()}')
