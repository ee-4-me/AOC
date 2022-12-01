import sys
sys.path.insert(0, '../../')
import os
import math
from helper.helper import getFile, mymap, myfilter

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    sum = 0

    for index in range(len(data)):
        line = data[index]

        a, b, c = mymap(myfilter(line.split(' '), lambda x: x != ''), lambda x: int(x))

        if a + b > c and a + c > b and b + c > a:
            sum += 1
        
    return sum 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    sum = 0

    for i in range(3):
        for index in range(0, len(data), 3):

            a = int(myfilter(data[index].split(' '), lambda x: x != '')[i])
            b = int(myfilter(data[index + 1].split(' '), lambda x: x != '')[i])
            c = int(myfilter(data[index + 2].split(' '), lambda x: x != '')[i])

            if a + b > c and a + c > b and b + c > a:
                sum += 1
        
    return sum 

print(f'part1: {part1()}')
print(f'part2: {part2()}')
