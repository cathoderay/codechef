"""
  Url: https://www.codechef.com/problems/AMMEAT
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


from math import inf


for _ in range(int(input())):
    N, M = list(map(int, input().split()))
    P = list(map(int, input().split()))

    mini = inf
    for i in range(2**N):
        suma = 0
        k = format(i, '0%db' % N)
        p = 0
        for i, j in enumerate(k):
            if j == '1':
                suma += P[i]
                p += 1
        if suma >= M and p < mini:
            mini = p 
    print(mini if mini != inf else -1)
