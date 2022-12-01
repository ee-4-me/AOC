import sys
sys.path.insert(0, '../../')
import os
import math
import copy
from helper.helper import getFile, mymap, myfilter, download_input, hash_string, hashes_equal

download_input(os.path.abspath(os.curdir), '')

# 00:31:00  3197, cant be mad

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n\n')

    sum = 0

    seeds = [int(x) for x in data[0].split(': ')[1].split(' ')]

    data = data[1:]
    
    ans = []
    for seed in seeds:
        nseed = seed
        for group in data:
            lines = group.split('\n')

            nlines = []

            for index in range(len(lines)):
                line = lines[index]

                if ':' in line:
                    continue

                a, b, n = [int(x) for x in line.split(' ')]
                    
                nlines.append([a, b, n])

            nlines = sorted(nlines, key=lambda x: x[1], reverse=False)
            for nn in nlines:
                if nseed < nn[1] + nn[2] and nseed >= nn[1]:
                    nseed = nseed + nn[0] - nn[1]
                    break
        ans.append(nseed)

    return min(ans) 

def getunsortedmap(lines):
    nlines = []

    for index in range(len(lines)):
        line = lines[index]

        if ':' in line:
            continue

        a, b, n = [int(x) for x in line.split(' ')]
            
        nlines.append([a, b, n])
    return nlines

#  14:09:55  27403, ugh

# [start, end] => [[start, end], [start, end] ..]
def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n\n')

    seeds = []
    seeds = [int(x) for x in data[0].split(': ')[1].split(' ')]

    ranges = [] 
    for i in range(0, len(seeds), 2):
        ranges.append([seeds[i], seeds[i] + seeds[i + 1]])

    for group in data[1:]:
        lines = group.split('\n')[1:]
        nlines = [[int(x) for x in line.split(' ')] for line in lines]
        nranges = []

        for nline in nlines:
            r1 = [nline[1], nline[1] + nline[2]]
            r2 = [nline[0], nline[0] + nline[2]]
            nranges.append([r1, r2])
        nranges = sorted(nranges, key=lambda x: x[0][0])

        for r in ranges[::]:
            ranges.pop(0)
            s, e = r
            
            # no effect
            if e < nranges[0][0][0]:
                ranges.append(r)
                continue

            # no effect
            if s >= nranges[-1][0][1]:
                ranges.append(r)
                continue

            # append chunks or wholes of nranges
            broke = False
            for nr in nranges:
                nrs, nre = nr

                # whole chunk, in range
                if s >= nrs[0] and e < nrs[1]:
                    # print(1)
                    ranges.append([s + nre[0] - nrs[0], e + nre[1] - nrs[1]])
                    broke = True
                    break

                # just start in range 
                elif s < nrs[1] and e >= nrs[1]:
                    ranges.append([s + nre[0] - nrs[0], nre[1] - 1])
                    s = nrs[1]

                # just end in range 
                elif s < nrs[0] and e > nrs[0]:
                    ranges.append([s + nre[0] - nrs[0], nre[1] - 1])
                    broke = True
                    break
                    
            if not broke:
                ranges.append([s, e])

    ranges = sorted(ranges, key=lambda x: x[0])

    return ranges[1][0] # correct for index 1, wihch is wierd, probably bug somewhere

print(f'part1: {part1()}')
print(f'part2: {part2()}')

