"""
  Url: https://www.codechef.com/problems/SAKTAN
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    N, M, Q = map(int, input().split())
    r = [0 for _ in range(N)]
    c = [0 for _ in range(M)]
    for _ in range(Q):
        R, C = map(int, input().split())
        r[R-1] += 1
        c[C-1] += 1
    co = len([j for j in c if j & 1])
    ce = M - co
    ac = 0
    for i in r: ac += co if i & 1 == 0 else ce
    print(ac)
