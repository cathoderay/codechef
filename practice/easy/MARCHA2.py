"""
  Url: https://www.codechef.com/problems/MARCHA2
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


import sys

for _ in range(int(input())):
    k = int(input())
    b = list(map(int, sys.stdin.readline().strip().split()))
    s = 1.0
    for i in range(k):
        if b[i] > s or s == 0:
            print('No')
            break
        s = (s - b[i]) * 2
    else:
        print('Yes' if s == 0 else 'No')
