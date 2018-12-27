"""
  Url: https://www.codechef.com/problems/BROKPHON
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    s = set()
    for i in range(1, N):
        if A[i] != A[i-1]:
            s.add(i+1)
            s.add(i)
    print(len(s))

