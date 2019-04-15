"""
  Url: https://www.codechef.com/problems/SUBREM.py
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"
    

def solve(V, E, X):
    stack = [0]
    while stack:
        cur = stack[-1]
        V[cur][2] = True
        if E[cur]:
            child = E[cur].pop()
            if V[child][2]: continue
            V[child][0] = cur
            stack.append(child)
            continue
        else:
            leaf = stack.pop()
            new_value = max(V[leaf][1], -X)
            V[leaf][1] = new_value
            parent = V[leaf][0]
            if parent is not None:
                V[parent][1] += new_value
    print(V[0][1])


for _ in range(int(input())):
    N, X = list(map(int, input().split()))
    A = list(map(int, input().split()))
    E = [[] for _ in range(N)] 
    for _ in range(N-1):
        u, v = list(map(int, input().split()))
        E[u-1].append(v-1)
        E[v-1].append(u-1)
    V = [[None, A[i], False] for i in range(N)]
    solve(V, E, X)
