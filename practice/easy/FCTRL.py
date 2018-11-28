"""
  Url: https://www.codechef.com/problems/FCTRL
"""

import sys


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


readline = lambda: sys.stdin.readline()

t = int(readline())
while t:
    n = int(readline())
    count = 0
    step = 5
    while n >= step:
        count += n//step
        step *= 5
    t -= 1
    print(int(count))

