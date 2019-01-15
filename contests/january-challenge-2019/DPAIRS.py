"""
  Url: https://www.codechef.com/problems/DPAIRS
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


N, M = list(map(int, input().split()))
A = enumerate(list(map(int, input().split())))
B = enumerate(list(map(int, input().split())))

A = sorted(A, key=lambda a: a[1])
B = sorted(B, key=lambda b: b[1])

for j in range(M):
    print(A[0][0], B[j][0])

for i in range(1, N):
    print(A[i][0], B[-1][0])
