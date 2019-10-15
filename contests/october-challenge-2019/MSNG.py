"""
  Url: https://www.codechef.com/problems/MSNG
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


def pos(a):
    x = set()
    for i in range(2, 37):
        try:
            x.add(int(a, i))
        except ValueError:
            continue
    return x


for _ in range(int(input())):
    P = []
    N = int(input())
    for _ in range(N):
        B, Y = input().split()
        P.append((int(B), Y))

    p = P.pop(0) 
    c = pos(p[1]) if p[0] == -1 else set([int(p[1], p[0])])

    for p in P:
        a, b = p[1], p[0]
        t = pos(a) if b == -1 else set([int(a, b)])
        c = c.intersection(t) 
        if len(c) == 0:
            break

    p = list(filter(lambda x: x <= 1000000000000, c))
    print(min(p) if p else -1)
