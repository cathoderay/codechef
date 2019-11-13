"""
  Url: https://www.codechef.com/problems/FAILURE
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


from functools import reduce


def path(root, p, v):
    pa = [v]
    while v != root:
        pa.append(p[v]) 
        v = p[v]
    return pa


def path_to_k(px, k, p):
    for i in px:
        if i == k: break
        p.append(i) 
    return p


def gcycle(pa, pb):
    p, a, b, k = [], set(pa), set(pb), None
    x = pa if len(pa) < len(pb) else pb
    for i in x:
        p.append(i)
        if i in a and i in b:
            k = i
            break
    p = path_to_k(pb if x == pa else pa, k, p)
    return frozenset(p)


def is_robust(N, E, root=0, to_remove=None):
    if to_remove == 0: root = 1 

    WHITE, GRAY, BLACK = 0, 1, 2
    not_visited = set(i for i in range(N))
    not_visited.remove(root)
    k, cycles, ccycles = 0, set(), set()

    m = [WHITE]*N
    m[root] = GRAY

    p = [root] + [0]*(N - 1)
    s = [root]

    while s:
        cur = s[-1]
        if m[cur] == BLACK:
            s.pop()
            if not s:
                while not_visited:
                    x = not_visited.pop()
                    if x != to_remove:
                        s.append(x)
                        k += 1
                        break
            continue
        for i in E[cur]:
            if i == to_remove:
                continue

            if m[i] == WHITE:
                p[i] = cur
                m[i] = GRAY
                not_visited.remove(i)
                s.append(i)
            else:
                if i != p[cur]:
                    pa = path(root, p, i)
                    pb = path(root, p, cur)
                    cycles.add(gcycle(pa, pb))
                    ccycles.add(k)
        m[cur] = BLACK
    return cycles, ccycles


for _ in range(int(input())):
    N, M = map(int, input().split())  
    E = [set() for i in range(N)]

    for _ in range(M):
        u, v = map(int, input().split())
        E[u-1].add(v-1)
        E[v-1].add(u-1)

    cycles, ccycles = is_robust(N, E)

    if not cycles or len(ccycles) > 1:
        print(-1)
        continue

    for i in sorted(list(reduce(lambda x, y: x & y, cycles))):
        cycles, _ = is_robust(N, E, to_remove=i)
        if not cycles:
            print(i+1)
            break
    else:
        print(-1)
