"""
  Url: https://www.codechef.com/problems/CHEFGR
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


for _ in range(int(input())):
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    print("Yes" if ((sum(A) + M) % N) == 0 else "No")
