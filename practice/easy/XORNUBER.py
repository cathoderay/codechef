"""
  Url: https://www.codechef.com/problems/XORNUBER
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


def is_2n(n):
    return n & (n - 1) == 0


for _ in range(int(input())):
    N = int(input())
    if N == 1:
        print(2)
    elif is_2n(N + 1):
        print(N // 2)
    else:
        print(-1)
 
