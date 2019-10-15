"""
  Url: https://www.codechef.com/problems/EVEDG
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    N, M = map(int, input().split())
    E = [set() for _ in range(N)]
    D = [0 for _ in range(N)]
    A = 0
    for _ in range(M):
        u, v = map(int, input().split())
        E[u-1].add(v-1)
        E[v-1].add(u-1)
    
    odd_edge = []
    for i in range(N):
        D[i] = len(E[i])
        A += D[i]
        if D[i] & 1:
            odd_edge.append(i)

    if not (A//2) & 1:
        print(1)
        print(*[1 for _ in range(N)])
        continue
    
    P = []
    if len(odd_edge):
        P.append({odd_edge[0]: 1})
        P2 = {}
        for i in range(N):
            if i != odd_edge[0]:
                P2[i] = 2
        P.append(P2)
    else:
        v = None
        for i in range(N):
            if len(E[i]) > 0:
                x, y = i, E[i].pop()
                P.append({x: 1})
                P.append({y: 2})
                break
        P3 = {}
        for i in range(N):
            if (i != x and i != y):
                P3[i] = 3
        P.append(P3)

    print(len(P))

    for i in range(N):
        for p, j in enumerate(P):
            if i in j:
                print(p + 1, end=' ')
    print()
