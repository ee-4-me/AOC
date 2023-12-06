import sys
sys.path.insert(0, '../../')
import os
import math
from helper.helper import getFile, mymap, myfilter, download_input

download_input(os.path.abspath(os.curdir))

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()
    data = data.split('\n')

    sum = 0

    for index in range(len(data)):
        line = data[index]

        allwords = line.split('[')[0].split('-')

        check = line.split('[')[1].split(']')[0]
        num = int(allwords[-1])
        words = allwords[:-1]

        h = {}
        for word in words:
            for c in word:
                if c in h:
                    h[c] += 1
                else:
                    h[c] = 1
        a = []
        for c in h:
            a.append([h[c], c])
                              
        if len(a) < len(check):
            continue

        a = sorted(a, key=lambda x: x[1])
        a = sorted(a, key=lambda x: x[0], reverse=True)

        flag = True
        for i in range(len(check)):
            c = check[i]
            if a[i][1] != c:
                flag = False
                break

        if flag:
            sum += num
        
    return sum 

def part2():
    data = getFile(input_path).strip()

    data = data.split('\n')

    for index in range(len(data)):
        line = data[index]

        allwords = line.split('[')[0].split('-')
        num = int(allwords[-1])

        line = list(line)
        for i in range(len(line)):
            c = line[i]
            x = (ord(c) - 97 + num) % 26 + 97
            line[i] = chr(x)

        line = ''.join(line)

        if line.startswith('north'):
            return num

print(f'part1: {part1()}')
print(f'part2: {part2()}')
