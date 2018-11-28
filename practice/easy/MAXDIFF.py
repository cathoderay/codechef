"""
  Url: https://www.codechef.com/problems/MAXDIFF
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    N, K = list(map(int, input().split()))

    ns = list(map(int, input().split()))

    ns.sort()

    if (N - K) < K:
        K = N - K

    print(abs(sum(ns[:K]) - sum(ns[K:])))
    

