"""
  Url: https://www.codechef.com/problems/TAVISUAL
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    N, C, Q = list(map(int, input().split()))
    for _ in range(Q):
        L, R = list(map(int, input().split()))
        if C <= R and C >= L:
            C = L + (R-C)
    print(C)

