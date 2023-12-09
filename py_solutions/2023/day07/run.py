import sys
sys.path.insert(0, '../../')
import os
import math
import copy
from helper.helper import getFile, mymap, myfilter, download_input, hash_string, hashes_equal

# super slopy, misread the prompt, tried to sort like normal poker hands, tooks a few days to come back to

download_input(os.path.abspath(os.curdir))

h = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
}

def gethand(s):
    hh = hash_string(s)
    freq = []
    for k in hh:
        freq.append(hh[k])

    if 5 in freq:
        return 7
    if 4 in freq:
        return 6
    if 3 in freq and 2 in freq:
        return 5
    if 3 in freq and len(freq) == 3:
        return 4
    if 2 in freq and len(freq) == 3:
        return 3
    if 2 in freq:
        return 2
    return 1

def wininhand(hand):
    return h[hand[0]] * 100000000 + h[hand[1]] * 1000000 + h[hand[2]] * 10000 + h[hand[3]] * 100 + h[hand[4]]

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    a = []
    for index in range(len(data)):
        line = data[index]
        hand, bid = line.split(' ')
        bid = int(bid)
        a.append([hand, bid])

    a = sorted(a, key=lambda x: wininhand(x[0]))
    a = sorted(a, key=lambda x: gethand(x[0]))

    sum = 0
    for i in range(len(a)):
        sum += (i + 1) * a[i][1]
    return sum 

h = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 1,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
}

def gethand2(s):
    hh = hash_string(s)

    if 'J' in hh:
        # move j's to most frequent spot
        m = [-1, -1]
        for k in hh:
            if k != 'J' and hh[k] > m[0]:
                m = [hh[k], k]

        if m[0] != -1:
            hh[m[1]] += hh['J']
            hh.pop('J', None)

    freq = []
    for k in hh:
        freq.append(hh[k])


    if 5 in freq:
        return 7
    if 4 in freq:
        return 6
    if 3 in freq and 2 in freq:
        return 5
    if 3 in freq and len(freq) == 3:
        return 4
    if 2 in freq and len(freq) == 3:
        return 3
    if 2 in freq:
        return 2
    return 1

def wininhand2(hand):
    return h[hand[0]] * 100000000 + h[hand[1]] * 1000000 + h[hand[2]] * 10000 + h[hand[3]] * 100 + h[hand[4]]

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    a = []
    for index in range(len(data)):
        line = data[index]
        hand, bid = line.split(' ')
        bid = int(bid)
        a.append([hand, bid])

    a = sorted(a, key=lambda x: wininhand2(x[0]))
    a = sorted(a, key=lambda x: gethand2(x[0]))

    sum = 0
    for i in range(len(a)):
        sum += (i + 1) * a[i][1]
    return sum 

print(f'part1: {part1()}')
print(f'part2: {part2()}')
