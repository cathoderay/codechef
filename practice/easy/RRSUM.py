"""
  Url: https://www.codechef.com/problems/RRSUM
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"
    

import sys


N, M = list(map(int, sys.stdin.readline().split()))
for i in range(M):
    q = int(sys.stdin.readline())
    r = 0
    if q < N + 2: 
        r = 0
    elif q == 2*N + 1:
        r = N
    elif q <= 2*N:
        r = q - N - 1
    elif q > 2*N + 1:
        r = 3*N - q + 1
    print(r)
