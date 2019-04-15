"""
  Url: https://www.codechef.com/problems/XORMIN.py
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


from math import inf

 
def build_traversal(e, m, s, i):
    r = []
    stack = [0]
    p = {}
    j = -1
    prev = 0
    while stack:
        cur = stack[-1]
        if not m[cur]:
            m[cur] = True
            j += 1
            r.append(cur)
            i[cur] = j
        if e[cur]:
            child = e[cur].pop()
            if m[child]: continue
            p[child] = cur
            stack.append(child)
            continue
        leaf = stack.pop()
        s[leaf] += 1
        if leaf in p and p[leaf]:
            s[p[leaf]] += s[leaf]
    return r, s, i


def solve(r, n, w, k, pos):
    pos = i[v]
    maxi = (inf, -1)
    for node in r[pos:pos+n]:
        n_w = w[node] ^ k 
        if (n_w > maxi[1] or 
            (n_w == maxi[1] and node < maxi[0])):
             maxi = (node, n_w)
    return maxi


for _ in range(int(input())):
    N, Q = list(map(int, input().split()))
    w = list(map(int, input().split()))
    e = [[] for i in range(N)]
    for _ in range(N - 1):
        x, y = list(map(int, input().split()))
        e[x-1].append(y-1)
        e[y-1].append(x-1)
    m = [False for _ in range(N)]
    s = [0 for _ in range(N)]
    i = [0 for _ in range(N)]
    s[0] = N - 1
    r, s, i = build_traversal(e, m, s, i)
    xl = vl = 0
    for _ in range(Q):
        a, b = list(map(int, input().split()))
        v, k = a ^ xl, b ^ vl
        v -= 1
        xl, vl = solve(r, s[v], w, k, i[v])
        xl += 1
        print(xl, vl)

