"""
  Url: https://www.codechef.com/problems/CNOTE
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"

import sys

read = sys.stdin.readline

for _ in range(int(input())):
    X, Y, K, N = list(map(int, read().split()))

    flag = 0
    for i in range(N):
        p, c = list(map(int, read().split()))
        if p + Y >= X and c <= K:
            flag = 1
    if flag: 
        print("LuckyChef")
    else:
        print("UnluckyChef")
