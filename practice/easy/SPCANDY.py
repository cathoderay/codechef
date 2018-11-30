"""
  Url: https://www.codechef.com/problems/SPCANDY
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    N, K = list(map(int, input().split()))
    if K == 0:
        print(0, N)
    else:
        print(N//K, N % K)
