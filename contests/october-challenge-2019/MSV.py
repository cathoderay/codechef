"""
  Url: https://www.codechef.com/problems/MSV
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


from functools import lru_cache
from sys import stdin
from collections import defaultdict


sqr = [pow(i, 0.5) for i in range(1000000 + 1)]


@lru_cache(maxsize=None)
def divisors(n):
    d = []
    i = 1
    p = 2 if n % 2 == 1 else 1
    while i <= sqr[n]:
        if n % i == 0:
            if (i != n // i):
                d.append(i)
                d.append(n//i)
            else:
                d.append(i)
        i += p
    return d


for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))

    maxi = 0
    d = defaultdict(int)
    for i in range(0, N):
        maxi = max(maxi, d[A[i]])
        for j in divisors(A[i]):
            d[j] += 1
    print(maxi)
