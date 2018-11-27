"""
    Url: https://www.codechef.com/problems/USF
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


# distinct factors using sieve of eratosthenes
lim = 10**5
p = [0]*(lim+3) 
for i in range(2, lim+1):
    if p[i] == 0:
        for k in range(i, lim+1, i):
            p[k] += 1


for _ in range(int(input())):
    n = input() 
    ns = list(map(int, input().split()))
    maxN = max(ns)

    vs = [0]*(maxN+3)

    for i in ns: vs[i] += 1

    maxi = 0
    for g in range(2, maxN+1):
        size = 0
        for k in range(g, maxN+1, g):
            size += vs[k]
        if (p[g]*size) > maxi:
            maxi = p[g]*size
    print(maxi)
