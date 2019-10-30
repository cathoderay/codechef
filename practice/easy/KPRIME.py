"""
  Url: https://www.codechef.com/problems/KPRIME
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


from collections import defaultdict


MAX_N = 10**5 + 1


def dfactors(n):
    factors = [0]*n
    p = 2
    while (p < n):
        if factors[p] == 0:
            for i in range(p, n, p):
                factors[i] += 1
        p += 1
    return factors


def prefix_sum(data):
    pre = defaultdict(list)
    pre[0] = [0]*6
    for i in range(1, MAX_N):
        pre[i] = pre[i-1][:]
        k = factors[i]
        if 1 <= k <= 5:
            pre[i][k] += 1
    return pre


factors = dfactors(MAX_N)
pre = prefix_sum(factors)
for _ in range(int(input())):
    A, B, K = map(int, input().split())
    print(pre[B][K]-pre[A-1][K])
