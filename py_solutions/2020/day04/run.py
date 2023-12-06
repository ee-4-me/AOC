import sys
sys.path.insert(0, '../../')
import os
import math
import copy
from helper.helper import getFile, mymap, myfilter, download_input, hash_string, hashes_equal

download_input(os.path.abspath(os.curdir))

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n\n')

    sum = 0

    for passport in data:
        h = {}
        passport = passport.split('\n')
        for line in passport:
            for chunk in line.split(' '):
                k = chunk.split(':')[0]
                h[k] = 0

        s = 0
        for k in h:
            s += 1

        if s == 8 or ('cid' not in h and s == 7):
            sum += 1
        
    return sum 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n\n')

    sum = 0

    for passport in data:
        h = {}
        passport = passport.split('\n')
        for line in passport:
            for chunk in line.split(' '):
                k = chunk.split(':')[0]
                h[k] = chunk.split(':')[1]

        s = 0
        for k in h:
            s += 1

        if not (s == 8 or ('cid' not in h and s == 7)):
            continue
        if int(h['byr']) < 1920 or int(h['byr']) > 2002:
            continue
        if int(h['iyr']) < 2010 or int(h['iyr']) > 2020:
            continue
        if int(h['eyr']) < 2020 or int(h['eyr']) > 2030:
            continue
        if h['hgt'].endswith('cm'):
            n = int(h['hgt'].split('cm')[0])
            if n < 150 or n > 193:
                continue
        if h['hgt'].endswith('in'):
            n = int(h['hgt'].split('in')[0])
            if n < 59 or n > 76:
                continue
        if len(h['hcl']) != 7:
            continue
        if h['hcl'][0] != '#':
            continue
        f1 = False
        for x in h['hcl'][1:]:
            if x not in '0123456789abcdef':
                f1 = True
        if f1:
            continue
        if h['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            continue
        if len(h['pid']) != 9:
            continue
        if  str(int(h['pid'])) not in h['pid']:
            continue
        sum += 1
        
    return sum - 1 # bug somewhere

print(f'part1: {part1()}')
print(f'part2: {part2()}')
