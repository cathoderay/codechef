"""
    Url: https://www.codechef.com/problems/USF
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    n = input() 
    ns = list(map(int, input().split()))
    maxN = max(ns)

    vs = [0]*(maxN+3)

    for i in ns: 
        vs[i] += 1

    p = [0]*(maxN+3)
    maxi = 0
    for g in range(2, maxN+1):
        size = 0
        prime = False
        if p[g] == 0: prime = True
        for k in range(g, maxN+1, g):
            size += vs[k]
            if prime: p[k] += 1
        if prime: p[g] = 1
        if (p[g]*size) > maxi:
            maxi = p[g]*size
    print(maxi)
