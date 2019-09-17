"""
  Url: https://www.codechef.com/problems/LAPD
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


from functools import reduce


MAX = 1000000007
sqr = [pow(i, 2) for i in range(5001)]


def solve(b, A, C):
    x = 0
    for a in range(min(b + 1, A), 1, -1):
        x += max(0, C - (sqr[b] + a - 1)//(a - 1))
    return x 


for _ in range(int(input())):
    A, B, C = list(map(int, input().split()))
    r = 0
    for b in range(B, 0, -1):
        r += (max(0, (C - b - 1))*max(0, (A - b - 1)))
        r += solve(b, A, C) + solve(b, C, A)
    print(r % MAX)
