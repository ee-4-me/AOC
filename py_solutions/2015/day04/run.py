import hashlib
import sys
sys.path.insert(0, '../../')
import os
import math
from helper.helper import getFile, mymap, myfilter, download_input
from hashlib import md5

def part1():
    data = 'yzbqklnj'

    i = 0
    while True:

      h = hashlib.new('md5')
      h.update((data + str(i)).encode('utf8'))
      a = h.hexdigest()
      if a.startswith('00000'):
        return i
      i += 1

def part2():
    data = 'yzbqklnj'

    i = 0
    while True:

      h = hashlib.new('md5')
      h.update((data + str(i)).encode('utf8'))
      a = h.hexdigest()
      if a.startswith('000000'):
        return i
      i += 1

print(f'part1: {part1()}')
print(f'part2: {part2()}')
