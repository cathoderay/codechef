"""
  Url: https://www.codechef.com/problems/SALARY
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


import operator


for _ in range(int(input())):
    N = int(input())
    W = list(map(int, input().split()))

    print(sum(W) - N*min(W))
