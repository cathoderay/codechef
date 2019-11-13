"""
  Url: https://www.codechef.com/problems/PHCUL
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


from math import inf, sqrt
from sys import stdin, stdout


rn = lambda: map(int, stdin.readline().strip().split())
idist = lambda x1, y1, x2, y2: (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)


def mintoe(x, y, E, LE, me):
    mini = inf
    for i in range(0, 2*LE, 2):
        mini = min(mini, idist(x, y, E[i], E[i+1]))
    me[(x, y)] = sqrt(mini)
    return mini


s = []
for _ in range(int(input())):
    x, y = rn()
    N, M, K = rn()
    A = list(rn())
    C = list(rn()) 
    E = list(rn()) 
    me = {}

    for ai in range(0, 2*N, 2):
        mintoe(A[ai], A[ai+1], E, K, me)

    for ci in range(0, 2*M, 2):
        mintoe(C[ci], C[ci+1], E, K, me)

    mini = inf
    for ai in range(0, 2*N, 2):
        for ci in range(0, 2*M, 2):
            dac = idist(A[ai], A[ai+1], C[ci], C[ci+1])
            xya = idist(x, y, A[ai], A[ai+1])
            xyc = idist(x, y, C[ci], C[ci+1])
            cur = sqrt(xya) + me[(C[ci], C[ci+1])]
            cur2 = sqrt(xyc) + me[(A[ai], A[ai+1])]
            mini = min(mini, min(cur, cur2) + sqrt(dac))
    s.append(str(mini))
stdout.write('\n'.join(s))
