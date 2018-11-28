"""
  Url: https://www.codechef.com/problems/NUKES
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


A, N, K = list(map(int, input().split()))

for _ in range(K):
    print(A % (N + 1), end=" ")
    A = A // (N + 1)
