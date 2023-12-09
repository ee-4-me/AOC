
import sys
sys.path.insert(0, '../../')
import os
import math
import copy
from helper.helper import getFile, mymap, myfilter, download_input, hash_string, hashes_equal

download_input(os.path.abspath(os.curdir))

def countboard(board):
    s = 0
    for row in board:
        for cell in row:
            if cell != -1:
                s += cell
    return s

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n\n')

    nums = [int(x) for x in data[0].split(',')]

    boards = []
    for index in range(1, len(data)):
        group = data[index]
        board = []
        lines = group.split('\n')
        for line in lines:
            board.append([int(x) for x in myfilter(line.split(' '), lambda y: y != '')])
        boards.append(board)

    for n in nums:
        for k in range(len(boards)):
            for i in range(len(boards[k])):
                for j in range(len(boards[k][i])):
                    if boards[k][i][j] == n:
                        boards[k][i][j] = -1

            # rows
            for i in range(len(boards[k])):
                c = 0
                for j in range(len(boards[k][i])):
                    if boards[k][i][j] == -1:
                        c += 1
                if c == len(boards[k][i]):
                    return n * countboard(boards[k])

            # cols
            for j in range(len(boards[k][0])):
                c = 0
                for i in range(len(boards[k])):
                    if boards[k][i][j] == -1:
                        c += 1
                if c == len(boards[k][0]):
                    return n * countboard(boards[k])

# not efficent, but works
def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n\n')


    nums = [int(x) for x in data[0].split(',')]

    boards = []
    for index in range(1, len(data)):
        group = data[index]
        board = []
        lines = group.split('\n')
        for line in lines:
            board.append([int(x) for x in myfilter(line.split(' '), lambda y: y != '')])
        boards.append(board)

    ans = []
    h = {}
    for n in nums:
        for k in range(len(boards)):
            for i in range(len(boards[k])):
                for j in range(len(boards[k][i])):
                    if boards[k][i][j] == n:
                        boards[k][i][j] = -1

            # rows
            for i in range(len(boards[k])):
                c = 0
                for j in range(len(boards[k][i])):
                    if boards[k][i][j] == -1:
                        c += 1
                if c == len(boards[k][i]):
                    if k not in h:
                        ans.append(n * countboard(boards[k]))
                    h[k] = 1

            # cols
            for j in range(len(boards[k][0])):
                c = 0
                for i in range(len(boards[k])):
                    if boards[k][i][j] == -1:
                        c += 1

                if c == len(boards[k][0]):
                    if k not in h:
                        ans.append(n * countboard(boards[k]))
                    h[k] = 1

    return ans[-1]

print(f'part1: {part1()}')
print(f'part2: {part2()}')
