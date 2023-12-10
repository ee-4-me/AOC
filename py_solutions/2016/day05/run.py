import sys
sys.path.insert(0, '../../')
import os
import math
import copy
from helper.helper import getFile, mymap, myfilter, download_input, hash_string, hashes_equal
import hashlib

download_input(os.path.abspath(os.curdir))

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')
    data = str(data[0])
        
    i = 0
    a = ''
    while True:
        h = hashlib.new('md5')
        h.update((data + str(i)).encode())
        hex = h.hexdigest()
        if hex.startswith('00000'):
            a += hex[5]
            if len(a) == 8:
                return a
        i += 1

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')
    data = str(data[0])
        
    i = 0
    a = ['' for x in range(8)]
    while True:
        h = hashlib.new('md5')
        h.update((data + str(i)).encode())
        hex = h.hexdigest()
        if hex.startswith('00000'):
            if hex[5] in '01234567':
                if a[int(hex[5])] == '':
                    a[int(hex[5])] = hex[6]
                    if all([x != '' for x in a]):
                        return ''.join(a)
        i += 1

print(f'part1: {part1()}')
print(f'part2: {part2()}')
