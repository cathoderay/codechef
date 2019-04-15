"""
  Url: https://www.codechef.com/problems/SJ1
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


from math import gcd


def solve(e, v, m, k):
    s = []
    stack = [0]
    while stack:
        cur = stack[-1]
        k[cur] = True
        if e[cur]:
            child = e[cur].pop()
            if k[child]: continue
            is_leaf[cur] = False
            v[child] = gcd(v[cur], v[child])
            stack.append(child)
        else:
            cur = stack.pop()
            if is_leaf[cur]:
                v[cur] = gcd(v[cur], m[cur])
                s.append((cur, m[cur] - v[cur]))
    print(' '.join(map(lambda x: str(x[1]), 
                       sorted(s, key=lambda x: x[0]))))


for _ in range(int(input())):
    N = int(input())
    e = [[] for _ in range(N)]
    for _ in range(N-1):
        x, y = list(map(int, input().split()))
        e[x-1].append(y-1)
        e[y-1].append(x-1)
    v = list(map(int, input().split()))
    m = list(map(int, input().split()))
    k = [False for _ in range(N)]
    is_leaf = [True for _ in range(N)]
    solve(e, v, m, k)
