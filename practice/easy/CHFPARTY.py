"""
  Url: https://www.codechef.com/problems/CHFPARTY
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    _ = int(input())
    A = list(map(int, input().split()))
    C = [0]*(max(A) + 1)
    for a in A: C[a] += 1
    s = 0
    for i, v in enumerate(C):
        if s < i: break
        s += v
    print(s)
