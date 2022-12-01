import sys
sys.path.insert(0, '../../')
import os
import math
from helper.helper import getFile, mymap, myfilter, download_input

download_input(os.path.abspath(os.curdir), '')

def key(i, j):
    return f'{i} {j}'

def check(h, i, j):
    
    for k in [
        key(i - 1, j - 1),
        key(i - 1, j),
        key(i - 1, j + 1),
        key(i, j - 1),
        key(i, j + 1),
        key(i + 1, j - 1),
        key(i + 1, j),
        key(i + 1, j + 1),
        ]:
        if k in h and h[k] != '.' and not h[k].isdigit():
            return True
    return False

# 2686 - 27:52, good enough for me

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    sum = 0

    h = {}
    for i in range(len(data)):
        line = data[i]
        line += '.'
        for j in range(len(line)):
            h[f'{i} {j}'] = line[j]


    for i in range(len(data)):
        data[i] += '.'
        seen = False
        s = ''

        for j in range(len(data[i])):
            if data[i][j].isdigit():
                s += data[i][j]
                if check(h, i, j):
                    seen = True
            else:
                if seen and s != '':
                    sum += int(s)
                s = ''
                seen = False
        
    return sum 

# 5620 - 1:15:25, so much lovley garbage

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()
    data = data.split('\n')

    sum = 0

    e = ''
    for i in range(len(data[0]) + 4):
      e += '.'
    data.append(e)
    data.insert(0, e)

    for i in range(len(data)):
      data[i] += '.'
      data[i] = '.' + data[i]

    for i in range(len(data)):
        for j in range(len(data[i])):
            p = []
            if data[i][j] == '*':
                if data[i][j + 1].isdigit():
                    p.append([i, j + 1])
                if data[i][j - 1].isdigit():
                    p.append([i, j - 1])

                if data[i + 1][j - 1].isdigit() and data[i + 1][j].isdigit() and data[i + 1][j + 1].isdigit():
                    p.append([i + 1, j - 1])
                elif data[i + 1][j - 1].isdigit() and not data[i + 1][j].isdigit() and data[i + 1][j + 1].isdigit():
                    p.append([i + 1, j - 1])
                    p.append([i + 1, j + 1])
                elif not data[i + 1][j - 1].isdigit() and data[i + 1][j].isdigit() and not data[i + 1][j + 1].isdigit():
                    p.append([i + 1, j])
                elif not data[i + 1][j - 1].isdigit() and data[i + 1][j].isdigit() and data[i + 1][j + 1].isdigit():
                    p.append([i + 1, j])
                elif data[i + 1][j - 1].isdigit() and data[i + 1][j].isdigit() and not data[i + 1][j + 1].isdigit():
                    p.append([i + 1, j - 1])
                elif data[i + 1][j - 1].isdigit() and not data[i + 1][j].isdigit() and not data[i + 1][j + 1].isdigit():
                    p.append([i + 1, j - 1])
                elif not data[i + 1][j - 1].isdigit() and not data[i + 1][j].isdigit() and data[i + 1][j + 1].isdigit():
                    p.append([i + 1, j + 1])

                if data[i - 1][j - 1].isdigit() and data[i - 1][j].isdigit() and data[i - 1][j + 1].isdigit():
                    p.append([i - 1, j - 1])
                elif data[i - 1][j - 1].isdigit() and not data[i - 1][j].isdigit() and data[i - 1][j + 1].isdigit():
                    p.append([i - 1, j - 1])
                    p.append([i - 1, j + 1])
                elif not data[i - 1][j - 1].isdigit() and data[i - 1][j].isdigit() and not data[i - 1][j + 1].isdigit():
                    p.append([i - 1, j])
                elif not data[i - 1][j - 1].isdigit() and data[i - 1][j].isdigit() and data[i - 1][j + 1].isdigit():
                    p.append([i - 1, j])
                elif data[i - 1][j - 1].isdigit() and data[i - 1][j].isdigit() and not data[i - 1][j + 1].isdigit():
                    p.append([i - 1, j - 1])
                elif data[i - 1][j - 1].isdigit() and not data[i - 1][j].isdigit() and not data[i - 1][j + 1].isdigit():
                    p.append([i - 1, j - 1])
                elif not data[i - 1][j - 1].isdigit() and not data[i - 1][j].isdigit() and data[i - 1][j + 1].isdigit():
                    p.append([i - 1, j + 1])

                if len(p) == 2:
                    s = ['', '']
                    for points_index in range(2):
                        ii, jj = p[points_index]
                        st = jj
                        for g in range(10):
                            if not data[ii][jj - g].isdigit():
                                st = jj - g + 1
                                break
                        for g in range(10):
                            if data[ii][st + g].isdigit():
                                s[points_index] += data[ii][st + g]
                            else:
                                break
                    sum += int(s[0]) * int(s[1])

    return sum 


print(f'part1: {part1()}')
print(f'part2: {part2()}')
