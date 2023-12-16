import os
from os.path import isfile
import requests

from helper.cookie import SESSION_COOKIE

# define libraries here

def getFile(path):
    with open(path, 'r') as file:
        return file.read()

def myfilter(data, ld):
    return list(filter(ld, data))

def mymap(data, ld):
    return list(map(ld, data))

def binarySearch(arr, target):
    pass

def download_input(file_path):
    path = os.path.normpath(file_path)
    path_list = path.split(os.sep)
    day = int(path_list[-1][3:])
    year = path_list[-2]

    input_path = os.path.join(file_path, 'input.txt')
    if os.path.isfile(input_path):
        with open(input_path, 'r') as file:
            if file.read() != '':
                return

    url = f'https://adventofcode.com/{year}/day/{day}/input'
    cookies = {'session': SESSION_COOKIE}
    
    response = requests.get(url, cookies=cookies)
    
    if response.status_code == 200:
        with open(input_path, 'w') as file:
            file.write(response.text)
        print(f"Input for year {year} day {day} saved to input.txt")
    else:
        print(f"Failed to fetch input for Day {day}. Status code: {response.status_code}")


def hash_string(string):
    h = {}
    for c in string:
        if c in h:
            h[c] += 1
        else:
            h[c] = 1

    return h

def hashes_equal(h1, h2):
    for c in h1:
        if c not in h2:
            return False
        if h2[c] != h1[c]:
            return False

    for c in h2:
        if c not in h1:
            return False
        if h2[c] != h1[c]:
            return False

    return True

def key(i, j):
    return f'{i} {j}'

def key3(i, j, c):
    return f'{i} {j} {c}'

