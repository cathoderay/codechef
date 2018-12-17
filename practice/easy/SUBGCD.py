"""
  Url: https://www.codechef.com/problems/SUBGCD
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


from functools import reduce
from math import gcd


for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))

    print(len(A) if reduce(gcd, A) == 1 else -1)
