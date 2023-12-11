import sys
sys.path.insert(0, '../../')
import os
import math
import copy
from helper.helper import getFile, mymap, myfilter, download_input, hash_string, hashes_equal, key

download_input(os.path.abspath(os.curdir))

# 00:16:11 1394, can't be mad
def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    sum = 0

    er = []
    ec = []
    eer = ['.' for x in range(len(data) * 2)]

    s = 0
    g = []
    for index in range(len(data)):
        gg = []
        line = data[index]
        for c in line:
            gg.append(c)
            if c == '#':
                s += 1
        g.append(copy.deepcopy(gg))

    for i in range(len(g)):
        r = g[i]
        if '#' not in r:
            er.append(i)
    for j in range(len(g[0])):
        foo = []
        for i in range(len(g)):
            foo.append(g[i][j])

        if '#' not in foo:
            ec.append(j)

    ec.sort(reverse=True)
    er.sort(reverse=True)

    for e in er:
        g.insert(e, eer)

    for e in ec:
        for i in range(len(g)):
            g[i].insert(e, '')

    h = {}

    for i in range(len(g)):
        for j in range(len(g[0])):
            c = g[i][j]
            if c == '#':
                k = key(i, j)
                h[k] = 1
        
    hh = []
    for k in h:
        hh.append([int(x) for x in k.split(' ')])

    ans = []

    for i in range(len(hh)):
        for j in range(i + 1, len(hh)):
            sy, sx = hh[i]
            ey, ex = hh[j]
            d = abs(sy - ey) + abs(sx - ex)
            ans.append(d)

    for a in ans:
        sum += a

    return sum 

# 00:37:02 2938, lots of mistakes ate time, still happy
def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    sum = 0

    er = []
    ec = []

    g = []
    for index in range(len(data)):
        gg = []
        line = data[index]
        for c in line:
            gg.append(c)
        g.append(copy.deepcopy(gg))

    for i in range(len(g)):
        r = g[i]
        if '#' not in r:
            er.append(i)
    for j in range(len(g[0])):
        foo = []
        for i in range(len(g)):
            foo.append(g[i][j])

        if '#' not in foo:
            ec.append(j)

    ec.sort(reverse=True)
    er.sort(reverse=True)

    h = {}

    for i in range(len(g)):
        for j in range(len(g[0])):
            c = g[i][j]
            if c == '#':
                k = key(i, j)
                h[k] = 1
        
    hh = []
    for k in h:
        hh.append([int(x) for x in k.split(' ')])

    ans = []

    l = 1000000 - 1
    for i in range(len(hh)):
        for j in range(i + 1, len(hh)):
            sy, sx = hh[i]
            ey, ex = hh[j]
            
            yn = 0
            for e in er:
                if e > min(sy, ey) and e < max(sy, ey):
                    yn += 1
            xn = 0
            for e in ec:
                if e > min(sx, ex) and e < max(sx, ex):
                    xn += 1

            d = (max(sy, ey) - min(sy, ey) + yn * l) + (max(sx, ex) - min(sx, ex) + xn * l)
            ans.append(d)

    for a in ans:
        sum += a

    return sum 

print(f'part1: {part1()}')
print(f'part2: {part2()}')
