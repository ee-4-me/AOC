import sys
sys.path.insert(0, '../../')
import os
import math
import copy
from helper.helper import getFile, mymap, myfilter, download_input, hash_string, hashes_equal

download_input(os.path.abspath(os.curdir))

# 00:25:06   4952, started 10 mins in, pretty happy

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    sum = 0

    for index in range(len(data)):
        line = data[index]
        g = [[int(x) for x in line.split(' ')]]
        

        while True:
            flag = True
            for n in g[-1]:
                if n != 0:
                    flag = False
            if flag:
                break

            g.append([])
            for i in range(len(g[-2]) - 1):
                g[-1].append(g[-2][i + 1] - g[-2][i])
                
        a = 0
        for i in range(len(g) - 2, -1, -1):
            a = g[i][-1] + g[i + 1][-1]
            g[i].append(a)

        sum += a
        
    return sum 

# 00:29:29   4404

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    sum = 0

    for index in range(len(data)):
        line = data[index]
        g = [[int(x) for x in line.split(' ')]]
        

        while True:
            flag = True
            for n in g[-1]:
                if n != 0:
                    flag = False
            if flag:
                break

            g.append([])
            for i in range(len(g[-2]) - 1):
                g[-1].append(g[-2][i + 1] - g[-2][i])
                
        gg = copy.deepcopy(g)
        for i in range(len(gg)):
            gg[i] = gg[i][::-1]

        g = copy.deepcopy(gg)
        a = 0
        for i in range(len(g) - 2, -1, -1):
            a = g[i][-1] - g[i + 1][-1]
            g[i].append(a)

        sum += a
        
    return sum 

print(f'part1: {part1()}')
print(f'part2: {part2()}')
