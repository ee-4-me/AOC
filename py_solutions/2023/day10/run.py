import sys
sys.path.insert(0, '../../')
import os
import math
import copy
from helper.helper import getFile, mymap, myfilter, download_input, hash_string, hashes_equal

download_input(os.path.abspath(os.curdir))

def key(y, x):
    return f'{y} {x}'

# so much hot garbage, but I am happy I solved it

# 00:50:34   3377, super happy with this
def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    h = {}
    x = 0
    y = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            h[key(i, j)] = data[i][j]
            if data[i][j] == 'S':
                x = j
                y = i
        
    # need to look left up down right from start, and see where I return from, then we know which two are valid
    # dfs

    hs = {}
    points = [[y, x, 1]]

    while len(points):
        p = points.pop(0)

        yy = p[0]
        xx = p[1]
        walk = p[2]

        ds = {
            '|': [[-1, 0], [1, 0]],
            '-': [[0, -1], [0, 1]],
            'L': [[-1, 0], [0, 1]],
            'J': [[-1, 0], [0, -1]],
            'F': [[1, 0], [0, 1]],
            '7': [[1, 0], [0, -1]],
            '.': [],
            'S': [[-1, 0], [1, 0], [0, 1], [0, -1]],
        }
        acept = {
            '-1 0': ['F', '7', '|'],
            '1 0': ['J', 'L', '|'],
            '0 1': ['J', '7', '-'],
            '0 -1': ['F', 'L', '-'],
        }

        for d in ds[h[key(yy, xx)]]:
            dy, dx = d
            
            yyy = yy + dy
            xxx = xx + dx

            k = key(yyy, xxx)

            # off map
            if k not in h:
                continue

            if h[k] not in acept[key(dy, dx)]:
                continue

            if k in hs:
                continue

            hs[k] = 1
            points.append([yyy, xxx, walk + 1])

    return (len(hs) + 1) // 2

# 02:29:12   3342 super happy with this too
def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    h = {}
    x = 0
    y = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            h[key(i, j)] = data[i][j]
            if data[i][j] == 'S':
                x = j
                y = i

    hs = {}
    points = [[y, x, 1]]

    while len(points):
        p = points.pop(0)

        yy = p[0]
        xx = p[1]
        walk = p[2]

        ds = {
            '|': [[-1, 0], [1, 0]],
            '-': [[0, -1], [0, 1]],
            'L': [[-1, 0], [0, 1]],
            'J': [[-1, 0], [0, -1]],
            'F': [[1, 0], [0, 1]],
            '7': [[1, 0], [0, -1]],
            '.': [],
            'S': [[-1, 0], [1, 0], [0, 1], [0, -1]],
        }
        acept = {
            '-1 0': ['F', '7', '|'],
            '1 0': ['J', 'L', '|'],
            '0 1': ['J', '7', '-'],
            '0 -1': ['F', 'L', '-'],
        }

        for d in ds[h[key(yy, xx)]]:
            dy, dx = d
            
            yyy = yy + dy
            xxx = xx + dx

            k = key(yyy, xxx)

            # off map
            if k not in h:
                continue

            if h[k] not in acept[key(dy, dx)]:
                continue

            if k in hs:
                continue

            hs[k] = 1
            points.append([yyy, xxx, walk + 1])

    # need to do seonnd dfs, start in corners, count number of empty cells
    hs[key(y, x)] = 'S'
    ans = part22(hs, len(data), len(data[0]), h)

    return ans



def part22(hs, my, mx, h):
    # search in ring around the whole thing, that way get all area

    g = []
    for i in range(3 * my):
        gg = []
        for j in range(3 * mx):
            gg.append(' ')
        g.append(copy.deepcopy(gg))

    for i in range(my):
        for j in range(mx):
            c = '.'
            k = key(i, j)
            if k in hs:
                c = h[k]
            if c == '|':
                g[i * 3 + 0][j * 3 + 0] = ' '
                g[i * 3 + 0][j * 3 + 1] = '|'
                g[i * 3 + 0][j * 3 + 2] = ' '
                g[i * 3 + 1][j * 3 + 0] = ' '
                g[i * 3 + 1][j * 3 + 1] = '|'
                g[i * 3 + 1][j * 3 + 2] = ' '
                g[i * 3 + 2][j * 3 + 0] = ' '
                g[i * 3 + 2][j * 3 + 1] = '|'
                g[i * 3 + 2][j * 3 + 2] = ' '
            if c == '-':
                g[i * 3 + 0][j * 3 + 0] = ' '
                g[i * 3 + 0][j * 3 + 1] = ' '
                g[i * 3 + 0][j * 3 + 2] = ' '
                g[i * 3 + 1][j * 3 + 0] = '-'
                g[i * 3 + 1][j * 3 + 1] = '-'
                g[i * 3 + 1][j * 3 + 2] = '-'
                g[i * 3 + 2][j * 3 + 0] = ' '
                g[i * 3 + 2][j * 3 + 1] = ' '
                g[i * 3 + 2][j * 3 + 2] = ' '
            if c == 'L':
                g[i * 3 + 0][j * 3 + 0] = ' '
                g[i * 3 + 0][j * 3 + 1] = '|'
                g[i * 3 + 0][j * 3 + 2] = ' '
                g[i * 3 + 1][j * 3 + 0] = ' '
                g[i * 3 + 1][j * 3 + 1] = 'L'
                g[i * 3 + 1][j * 3 + 2] = '-'
                g[i * 3 + 2][j * 3 + 0] = ' '
                g[i * 3 + 2][j * 3 + 1] = ' '
                g[i * 3 + 2][j * 3 + 2] = ' '
            if c == 'J':
                g[i * 3 + 0][j * 3 + 0] = ' '
                g[i * 3 + 0][j * 3 + 1] = '|'
                g[i * 3 + 0][j * 3 + 2] = ' '
                g[i * 3 + 1][j * 3 + 0] = '-'
                g[i * 3 + 1][j * 3 + 1] = 'J'
                g[i * 3 + 1][j * 3 + 2] = ' '
                g[i * 3 + 2][j * 3 + 0] = ' '
                g[i * 3 + 2][j * 3 + 1] = ' '
                g[i * 3 + 2][j * 3 + 2] = ' '
            if c == '7':
                g[i * 3 + 0][j * 3 + 0] = ' '
                g[i * 3 + 0][j * 3 + 1] = ' '
                g[i * 3 + 0][j * 3 + 2] = ' '
                g[i * 3 + 1][j * 3 + 0] = '-'
                g[i * 3 + 1][j * 3 + 1] = '7'
                g[i * 3 + 1][j * 3 + 2] = ' '
                g[i * 3 + 2][j * 3 + 0] = ' '
                g[i * 3 + 2][j * 3 + 1] = '|'
                g[i * 3 + 2][j * 3 + 2] = ' '
            if c == 'F':
                g[i * 3 + 0][j * 3 + 0] = ' '
                g[i * 3 + 0][j * 3 + 1] = ' '
                g[i * 3 + 0][j * 3 + 2] = ' '
                g[i * 3 + 1][j * 3 + 0] = ' '
                g[i * 3 + 1][j * 3 + 1] = '7'
                g[i * 3 + 1][j * 3 + 2] = '-'
                g[i * 3 + 2][j * 3 + 0] = ' '
                g[i * 3 + 2][j * 3 + 1] = '|'
                g[i * 3 + 2][j * 3 + 2] = ' '
            if c == '.':
                g[i * 3 + 0][j * 3 + 0] = ' '
                g[i * 3 + 0][j * 3 + 1] = ' '
                g[i * 3 + 0][j * 3 + 2] = ' '
                g[i * 3 + 1][j * 3 + 0] = ' '
                g[i * 3 + 1][j * 3 + 1] = ' '
                g[i * 3 + 1][j * 3 + 2] = ' '
                g[i * 3 + 2][j * 3 + 0] = ' '
                g[i * 3 + 2][j * 3 + 1] = ' '
                g[i * 3 + 2][j * 3 + 2] = ' '
            if c == 'S':
                g[i * 3 + 0][j * 3 + 0] = 'S'
                g[i * 3 + 0][j * 3 + 1] = 'S'
                g[i * 3 + 0][j * 3 + 2] = 'S'
                g[i * 3 + 1][j * 3 + 0] = 'S'
                g[i * 3 + 1][j * 3 + 1] = 'S'
                g[i * 3 + 1][j * 3 + 2] = 'S'
                g[i * 3 + 2][j * 3 + 0] = 'S'
                g[i * 3 + 2][j * 3 + 1] = 'S'
                g[i * 3 + 2][j * 3 + 2] = 'S'
    o = ''
    for r in g:
        for c in r:
            o += c
        o += '\n'
    with open('bar.txt', 'w') as file:
        file.write(o)


    points = [[0, 0]] # found by looking at input
    v = {}
    v[key(0, 0)] = 1

    d = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    while len(points):
        p = points.pop()
        y, x = p

        for dd in d:
            dy, dx = dd
            yy = y + dy
            xx = x + dx

            kk = key(yy, xx)

            if yy < 0 or xx < 0 or yy >= my * 3 or xx >= mx * 3:
                continue

            if g[yy][xx] != ' ':
                continue

            if kk in v:
                continue

            v[kk] = 1
            points.append([yy, xx])

    blankoutside = 0
    for i in range(my):
        for j in range(mx):
            flag = True
            for k in range(3):
                for l in range(3):
                    ke = key(i * 3 + k, j * 3 + l)
                    if ke not in v:
                        flag = False
                    if g[i * 3 + k][j * 3 + l] != ' ':
                        flag = False
            if flag:
                blankoutside += 1

    return mx * my - blankoutside - len(hs)

print(f'part1: {part1()}')
print(f'part2: {part2()}')
