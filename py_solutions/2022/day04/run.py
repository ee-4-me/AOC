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

    sum = 0

    for index in range(len(data)):
        line = data[index]

        o,t = line.split(',')
        o1,o2 = o.split('-')
        t1,t2 = t.split('-')
        o1 = int(o1)
        o2 = int(o2)
        t1 = int(t1)
        t2 = int(t2)

        if (o1 >= t1 and o2 <= t2) or (t1 >= o1 and t2 <= o2):
            sum += 1
        
    return sum 

# not efficent, but it works
def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    sum = 0

    for index in range(len(data)):
        line = data[index]

        o,t = line.split(',')
        o1,o2 = o.split('-')
        t1,t2 = t.split('-')
        o1 = int(o1)
        o2 = int(o2)
        t1 = int(t1)
        t2 = int(t2)

        h = {}
        for i in range(o1, o2 + 1):
            h[i] = 1
        for i in range(t1, t2 + 1):
            if i in h:
                sum += 1
                break

    return sum 


print(f'part1: {part1()}')
print(f'part2: {part2()}')
