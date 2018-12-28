"""
  Url: https://www.codechef.com/problems/FIRESC
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


from functools import reduce
from collections import Counter


class UF:
    def __init__(self, N):
        self.p = list(range(0, N + 1))
        self.size = [1]*(N + 1)

    def find(self, a):
        while a != self.p[a]:
            a = self.p[a]
        return a

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb: return

        if self.size[pa] < self.size[pb]:
            self.p[pa] = pb
            self.size[pb] += self.size[pa]
            self.size[pa] = 1
        else:
            self.p[pb] = pa
            self.size[pa] += self.size[pb]
            self.size[pb] = 1


for _ in range(int(input())):
    N, M = list(map(int, input().split()))
    f = [tuple(map(int, input().strip().split())) for i in range(M)]

    uf = UF(N)
    for i in f: uf.union(*i)

    r = sum([1 if i == v else 0 for i, v in enumerate(uf.p)]) - 1
    s = reduce(lambda a, b: a*b % (10**9 + 7), uf.size)
    print(r, s)
