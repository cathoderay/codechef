"""
  Url: https://www.codechef.com/problems/ROWCOLOP
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


N, Q = list(map(int, input().split()))

R = [0]*N
C = [0]*N 

for q in range(Q):
    op, i, x = input().strip().split()
    if op.startswith('R'):
        R[int(i)-1] += int(x)
    else:
        C[int(i)-1] += int(x)
print(max(C) + max(R)) 

